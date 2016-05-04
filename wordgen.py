worddict = {}
alphabetmap = {}

def genwords(length):
    pass
def loadwords():
    wordfile = open("words.txt")
    words = wordfile.readlines()
    for word in words:
        wordlength = len(word)
        if worddict.has_key(wordlength):
            worddict[wordlength][word[0]] = word
        else:
            worddict[wordlength] = word

if __name__ == '__main__':
    loadwords()
