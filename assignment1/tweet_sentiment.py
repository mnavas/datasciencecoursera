import sys
import json
import re

def hw(sent_file,tweet_file):
	scores = {} # initialize an empty dictionary
	for line in sent_file:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	#print scores.items() # Print every (term, score) pair in the dictionary
	tw = {} #initialize an empty dictionary
	for line in tweet_file:
		score = 0
		try:
			tweet=json.loads(line)
			if 'lang' in tweet and tweet['lang'] == "en" and 'text' in tweet:
				text = tweet['text']
		    		text = text.encode('utf-8')
		    		for word in re.compile('\w+').findall(text):
					if word in scores:
						score = score + scores[word]
				print score
				
			else:
				print score
		except:
			print score

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
