import sys
import json
import re

def hw(sent_file,tweet_file):
	scores = {} # initialize an empty dictionary
	for line in sent_file:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	tw = {} #initialize an empty dictionary
	sw = {}
	for line in tweet_file:
		score = 0
		count = 0
		try:
			tweet=json.loads(line)
			if 'lang' in tweet and tweet['lang'] == "en" and 'text' in tweet:
				text = tweet['text']
		    		text = text.encode('utf-8')
		    		for word in re.compile('\w+').findall(text):
					if word in scores:
						count = count + 1
						score = score + scores[word]
				for word in re.compile('\w+').findall(text):
					if word not in scores:
						if word not in tw or word not in sw:
							tw[word] = 0
							sw[word] = 0
						tw[word] = tw[word] + count
						sw[word] = sw[word] + score
				
		except:
			score = 0
			count = 0
	for word in sw:
		score = 0
		if tw[word] > 0:
			score = float(sw[word])/float(tw[word])
		print "{} {}".format(word,score)
			

def lines(fp): 
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
