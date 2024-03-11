import nltk
#nltk.download('punkt')

from nltk.stem.porter import PorterStemmer
import numpy as nenbape

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    #stem is lowering and simpling words to one
    return stemmer.stem(word.lower())

def all_words_fun(tokenized_all_worlds_in_senteze, all_words):
    

    tokenized_all_worlds_in_senteze = [stem(w) for w in tokenized_all_worlds_in_senteze]
    bag = nenbape.zeros(len(all_words), dtype=nenbape.float32)

    for idx, w in enumerate(all_words):
        if w in tokenized_all_worlds_in_senteze:
            bag[idx] = 1.0

    return bag 

#sentece = ["hello", "word", "you", "are", "gay"]
#words = ["you", "max", "pefer", "gay", "liking"]
#print(all_words_fun(sentece, words))