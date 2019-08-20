import csv
from random import shuffle


def getWordsTuple(file, col=0, lowerbound=0):
	words = []
	with open(file) as f:
		wordreader = csv.reader(f, delimiter = ',')
		for row in wordreader:
			words.append(row[col].strip())
	shuffle(words)
	print (words[lowerbound])


word_csv_name = "SimpsonsFreq.csv"
col = 1
getWordsTuple(word_csv_name, col)