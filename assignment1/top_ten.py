import sys
import json
import re

def hw(tweet_file):
	hashtags = {} #initialize an empty dictionary
	count = 0
	for line in tweet_file:		
		try:
			tweet=json.loads(line)
			if 'entities' in tweet and 'hashtags' in tweet['entities']:
				for hashtag in tweet['entities']['hashtags']:
					text = hashtag['text'].encode('utf-8')
					if text not in hashtags:
						hashtags[text] = 0
					hashtags[text] = hashtags[text] + 1
		    		
		except:
			count = count
	for hashtag in sorted(hashtags, key=hashtags.get, reverse=True)[:10]:
		print "{} {}".format(hashtag,hashtags[hashtag])

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)


if __name__ == '__main__':
    main()
