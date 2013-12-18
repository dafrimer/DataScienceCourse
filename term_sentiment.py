import sys
import json
import re
scores = {} # initialize an empty dictionary
new_words = {}  #initialize new dictionary for storing new words
new_dict = {}


def dictionary(file):
    global scores
    afinnfile = file
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = float(score)  # Convert the score to an integer.

def tweets(file):
    global scores, new_words
    
    for line in file.readlines():    
        tweet = json.loads(line)
        tweet_score = 0
        if 'text' in tweet:
            spectweet = tweet['text'].encode('utf-8')
            #print spectweet +"\n"
            for word in re.split("!@#$%^&*:| ",spectweet.lower()):
                if word in scores.keys():
                    tweet_score += scores[word]
                    
            for word in set(re.split("!@#$%^&*:| ",spectweet.lower()))-set(scores.keys()): # word in new_words[word]:
                nwords = len(re.split("!@#$%^&*:| ",spectweet.lower()))
                key_id=0
                if word in new_words.keys():
                    key_id = len(new_words[word])
                    new_words[word][key_id]=tweet_score/nwords
                else:
                    new_words[word]= {}
                    new_words[word][0]=tweet_score/nwords

    new_dictionary()
#For each word in dictionary = (1/n)*SUM(i=1,n)[total score of tweet(i)/sum(words in tweet)]                    
def new_dictionary():
    global new_words, new_dictionary
    for word in new_words.keys():
        total_sum = 0
        for i in range(len(new_words[word].keys())-1):
            total_sum += new_words[word][i]
        average_score =  float(total_sum/len(new_words[word].keys()))
        new_dict[word] = average_score
    for word in new_words.keys():
        print word  + " " + str(new_dict[word])


    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    dictionary(sent_file)
    tweets(tweet_file)

if __name__ == '__main__':
    main()


