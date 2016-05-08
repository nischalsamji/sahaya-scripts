import cPickle as pickle

words = pickle.load(open( "worddict.pkl", "rb" ))
print words[7]['z']
