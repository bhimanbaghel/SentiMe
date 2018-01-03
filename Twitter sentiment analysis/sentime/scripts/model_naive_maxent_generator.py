import csv
import nltk
from nltk.classify import *
#import regex
import re
import pickle

#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end



#initialize stopWords
stopWords = []

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

#start getStopWordList
def getStopWordList(stopWordListFileName):
    #read the stopwords file and build a list
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')
    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
#end

#start getfeatureVector
def getFeatureVector(tweet,stopWords):
    featureVector = []
    #split tweet into words
    words = tweet.split()
    for w in words:
        #replace two or more with two occurrences
        w = replaceTwoOrMore(w)
        #strip punctuation
        w = w.strip('\'"?,.')
        #check if the word stats with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        #ignore if it is a stop word
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector
#end



#Read the tweets one by one and process it
inpTweets = csv.reader(open('./scripts/data/feature_list/max_ent.csv', 'r',encoding='latin-1'), delimiter=',')
stopWords = getStopWordList('./scripts/data/feature_list/stopwords.txt')
tweets = []
featureList = []
for row in inpTweets:
	if row:
		sentiment=row[0]
		tweet=row[1]
		processedTweet=processTweet(tweet)
		featureVector=getFeatureVector(processedTweet,stopWords)
		featureList.extend(featureVector)
		tweets.append((featureVector,sentiment))
		
#end loop

#print(tweets)

featureList = list(set(featureList))

#start extract_features
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features
#end


training_set = nltk.classify.util.apply_features(extract_features, tweets)

'''NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
pickle_out = open('classifier_naivebayes.pickle','wb')
pickle.dump(NBClassifier, pickle_out)
pickle_out.close() 
'''

classifier = nltk.classify.maxent.MaxentClassifier.train(training_set, 'GIS', trace=3, \
                                    encoding=None, labels=None, gaussian_prior_sigma=0, max_iter = 5) 
outfile = open('classifier_max_ent2.pickle', 'wb')        
pickle.dump(classifier, outfile)        
outfile.close()


# Test the classifier
testTweet = 'Congrats @ravikiranj, i heard you wrote a new tech post on sentiment analysis'
processedTestTweet = processTweet(testTweet)
print (classifier.classify(extract_features(getFeatureVector(processedTestTweet,stopWords))))
