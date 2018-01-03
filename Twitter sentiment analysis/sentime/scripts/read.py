import csv
inpTweets = csv.reader(open('./scripts/data/feature_list/full_training_dataset.csv', 'r',encoding='latin-1'), delimiter=',')

for row in inpTweets:
	print(row[0],row[1])