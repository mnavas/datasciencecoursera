import sys
import json
import re

def hw(tweet_file):
	tw = {} #initialize an empty dictionary
	count = 0
	for line in tweet_file:		
		try:
			tweet=json.loads(line)
			if 'lang' in tweet and tweet['lang'] == "en" and 'text' in tweet:
				text = tweet['text']
		    		text = text.encode('utf-8')
		    		for word in re.compile('\w+').findall(text):
					count = count + 1
					if word not in tw:
						tw[word] = 0
					tw[word] = tw[word] + 1
		except:
			count = count
	for word in tw:
		print "{} {}".format(word,float(tw[word])/float(count))

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)


if __name__ == '__main__':
    main()
