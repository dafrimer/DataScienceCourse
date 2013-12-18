import urllib
import json
import sys
import codecs

lines =str("change")
sent_file =open(sys.argv[1])
sent_file2=sent_file
def main():
    global lines
    #lines = str(len(sent_file.readlines()))
    #sent_file.close()
    #explain(lines)

def explain(fp):
    print str("what is going on")
    print type(fp)
    fp.close()


for i in range(205):        
    sent_fil2e = sent_file.readline()
    tweet = json.loads(sent_fil2e)
    if 'lang' in tweet:
        if tweet['lang'] == str("en"):
            #tweetdecode = tweetcode.encode('utf-8')
                print tweet['text'].encode('utf-8')
                
    
#print type(pyresponse)
#print
#print pyresponse.keys()
#print

#for i in range(10):
#    print pyresponse['results'][i]['text']
#    print

# Consumer Key:  w0IKN7egminDqjauuC45yg
# Consumer Secret: WR8LhFoVx1XQAIZUtIzvwr094zFlXN6TApR1O10qB44
# Access Token: 20349155-xr1BGqC1npCUz8AJrxQGX0hlaDSUjmSm5bLwiu8uY
# Access Token Scret: kRfnbbSUcHD06B9Ol826FligjXkwYFamed3fjqIVbiE

