from . import get_twitter_data
from . import naive_bayes_classifier,max_entropy_classifier

def main(search):
	twitterData=get_twitter_data.TwitterData()
	keyword=search
	time='today'
	tweets=twitterData.getTwitterData(keyword,time)
	print(tweets)
	trainingDataFile = './scripts/40_test_max_ent.csv'               
	classifierDumpFile = './scripts/classifier_naivebayes.pickle'
	trainingRequired=0

	nb = naive_bayes_classifier.NaiveBayesClassifier(tweets, keyword, time, trainingDataFile, classifierDumpFile, trainingRequired)
	acc = nb.classify()

	'''cl=max_entropy_classifier.MaxEntClassifier(tweets, keyword, time, trainingDataFile, classifierDumpFile, trainingRequired)
	acc = cl.accuracy()'''
	return acc