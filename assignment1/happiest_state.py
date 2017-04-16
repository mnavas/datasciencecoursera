import sys
import json
import re

def hw(sent_file,tweet_file):
	scores = {} # initialize an empty dictionary
	for line in sent_file:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	#print scores.items() # Print every (term, score) pair in the dictionary
	sst = {} #initialize an empty dictionary
	cst = {}
	for line in tweet_file:
		score = 0
		try:
			tweet=json.loads(line)
			if 'lang' in tweet and tweet['lang'] == "en" and 'text' in tweet and type(tweet['place']) is dict and tweet['place']['country'] == "United States":
				text = tweet['text']
		    		text = text.encode('utf-8')
				state = tweet['place']['full_name'].split(", ")[1]
				if state not in sst:
					sst[state] = 0
					cst[state] = 0
		    		for word in re.compile('\w+').findall(text):
					if word in scores:
						sst[state] = sst[state] + scores[word]
				cst[state] = cst[state] + 1
				
		except:
			score=0
	scores = {}
	for state in sst:
		scores[state] = float(sst[state])/float(cst[state])
	print max(scores, key=scores.get)

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
