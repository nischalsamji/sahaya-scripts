import enchant
import cPickle as pickle

d = enchant.Dict("en_US")

worddict = {}
alphabetmap = {}

def loadwords():
	letters = 'abcdefghijklmnopqrstuvwxyz'
	wordfile = open("words.txt")
	words = wordfile.readlines()
	for length in range(3,8):
		alphabetmap = {}
		for letter in range(len(letters)):
			letterwords = [word.rstrip('\n') for word in words if word[0] == letters[letter] and len(word) == length and d.check(word.rstrip('\n'))]
			alphabetmap[letters[letter]] = letterwords
		worddict[length] = alphabetmap
	pickle.dump( worddict, open( "worddict.pkl", "wb" ) )

if __name__ == '__main__':
	loadwords()
