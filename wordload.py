import cPickle as pickle
words = {}

def printwords(length, letter):
	print words[int(length)][letter]
	

if __name__ == '__main__':
	words = pickle.load(open( "worddict.pkl", "rb" ))
	length = raw_input('Enter the length of the words\n')
	letter = raw_input('Enter a character\n')
	printwords(length, letter)