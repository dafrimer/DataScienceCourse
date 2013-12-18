import sys
import json
scores = {} # initialize an empty dictionary

def dictionary(file):
    global scores
    afinnfile = file
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

def tweets(file):
    
    for line in file.readlines():    
        tweet = json.loads(line)
        tweet_score = 0
        if 'text' in tweet and ('lang' in tweet and tweet['lang']=="en"):
            spectweet = tweet['text'].encode('utf-8')
            
            for word in spectweet.lower().split():
                if word in scores.keys():
                    tweet_score += scores[word]
            
            print float(tweet_score)
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    dictionary(sent_file)
    tweets(tweet_file)

if __name__ == '__main__':
    main()


