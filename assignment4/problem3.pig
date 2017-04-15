register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

a_data = FILTER ntriples BY subject MATCHES '.*rdfabout.com.*';
a_unique = DISTINCT a_data;
b_data = FILTER ntriples BY subject MATCHES '.*rdfabout.com.*';
b_unique = DISTINCT b_data;

X = JOIN a_unique BY object, b_unique BY subject;
x_unique = DISTINCT X;

-- store the results in the folder /user/hadoop/example-results
store x_unique into '/user/hadoop/problem3-results' using PigStorage();
-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_object_ordered into 's3n://superman/example-results';
