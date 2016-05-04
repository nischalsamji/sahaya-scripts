worddict = {}
alphabetmap = {}

def genwords(length):

def loadwords():
    wordfile = open("words.txt")
    words = wordfile.readlines()
    for word in words:
        wordlength = len(word)
        if worddict.haskey(wordlength):
            wordict[wordlength][] = word
