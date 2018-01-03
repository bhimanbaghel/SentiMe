import json
import datetime
import urllib
import random
from datetime import timedelta
import pickle
import sys
from TwitterSearch import *

class TwitterData:
    #start __init__
    def __init__(self):
        self.currDate = datetime.datetime.now()

    def getTwitterData(self, keyword, time):
        self.weekTweets = {}
        if(time == 'today'):
            for i in range(0,1):
                currDate1 = datetime.date.today()
                tso = TwitterSearchOrder() # create a TwitterSearchOrder object
                tso.set_keywords([keyword]) # let's define all words we would like to have a look for
                tso.set_language('en') # we want to see German tweets only
                tso.set_until(currDate1)
                tso.set_result_type('recent')
                tso.set_include_entities(False) # and don't give us all those entity information

                ts = TwitterSearch(
                    consumer_key = "99efomlTCxiqLuUoHwbVCM2uq",
                    consumer_secret = "J4qboSQUzbFAw642aJdNMdK8z1F5pXvK7UjPA8ijMfxMUXDkAU",
                    access_token = "3243160872-8UzdKblVcvyy3RCS3NeAB1JaVnFX8plPClbVJhl",
                    access_token_secret = "ghtCpXXp7UGOTVKZSSBqMzktuRmBqsnVQEIV6oryaFXi5"
                )
                test_tweet=[]
                max_count=100

                for tweet in ts.search_tweets_iterable(tso):
                    if max_count>0:  
                      saveFile=open('virat.csv','a')
                      temp=tweet['text'].encode(sys.stdout.encoding, errors='replace')
                      test_tweet.append(temp)
                    max_count=max_count-1

    # it's about time to create a TwitterSearch object with our secret tokens
                self.weekTweets[i] = test_tweet
                filename = './scripts/data/weekTweets/weekTweets_'+urllib.parse.unquote(keyword.replace("+", " "))+'_'+str(int(random.random()*10000))+'.txt'
                outfile = open(filename, 'wb')        
                pickle.dump(self.weekTweets, outfile)        
                outfile.close()
            #end loop
        return self.weekTweets
    '''
        inpfile = open('data/weekTweets/weekTweets_obama_7303.txt')
        self.weekTweets = pickle.load(inpfile)
        inpfile.close()
        return self.weekTweets
    '''
    #end
        
    #end

    #start getWeeksData
     

#end clas