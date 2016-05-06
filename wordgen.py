worddict = {}
alphabetmap = {}

def genwords(length):
    pass
def loadwords():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    wordfile = open("words.txt")
    words = wordfile.readlines()
    for letter in range(len(letters)):
        letterwords = [word.rstrip('\n') for word in words if word[0] == letters[0] and len(word) == 4]
        alphabetmap['a'] = letterwords
        worddict[3] = alphabetmap
    print worddict
if __name__ == '__main__':
    loadwords()
    for i in range(3,6):
        genwords(i)
