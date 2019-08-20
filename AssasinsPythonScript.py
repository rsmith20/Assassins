import csv
from random import shuffle

# Opens CSV file "file", reads every word in "col", then takes
# only the words found within the bounds and returns them.
# The use of col is in case you actually have multiple values in your csv.



def getWordsTuple(file, col=0, lowerbound=0, upperbound=None):
	words = []
	with open(file) as f:
		wordreader = csv.reader(f, delimiter = ',')
		for row in wordreader:
			words.append(row[col].strip())
	words = words[lowerbound : upperbound] if upperbound != None else words[lowerbound:]
	return words

# Open CSV file "file", read first entry on each line and return the array.
# Note that all names must be distinct for future tasks.

def getNames(file):
	names = []
	with open(file) as f:
		wordreader = csv.reader(f, delimiter = ',')
		for row in wordreader:
			names.append(row[0].strip())
	return names



# Creates NUM_CYCLES games by permuting the list of names and then
# assigning targets in order with a random word for each player.
# Note this does NOT delete files, so if you already have files of this name
# TODO: Would be reasonable to have this create a directory and put everything inside it.
# TODO: Line endings based on OS?
def createGame(names, words, NUM_CYCLES):
	for y in range(0, NUM_CYCLES):
		shuffle(names)
		# Presumably this second shuffle is independent?
		shuffle(words)
		for x in range(0, len(names)):
			target = names[(x + 1) % len(names)]
			word = words[x]
			file = open(names[x] + "_info.txt", "a+")
			file.write("Your name is: " + names[x] + ". Your target in cycle " + str(y + 1) + " is: " + target + ". Your word is \"" + word + "\".\r\n")
			file.close()


		cycle = open("Cycle.txt", "a+")
		cycle.write("Cycle " + str(y + 1) + ".\r\n")

		for x in range(0, len(names)):
			target = names[(x + 1) % len(names)]
			word = words[x]
			cycle.write(names[x] + " has " + target + " with word: \"" + word + "\".\r\n")

		cycle.close()



MIN_WORD_RANK = 1000
MAX_WORD_RANK = 2000
NUM_CYCLES = 1
word_csv_name = "SimpsonsFreq.csv"
players_csv_name = "NamesExample.csv"
word_position = 1

# TODO: Find a better source of words, potentially by manually curating current list. 
# Then you can not use bounds and just have all good words.

words = getWordsTuple(word_csv_name, word_position, MIN_WORD_RANK, MAX_WORD_RANK)
names = getNames(players_csv_name)
createGame(names, words, NUM_CYCLES)


# TODO: Integrate with a webserver and potentially twilio for easy games.
# TODO: Reasonable to make some command line parameters