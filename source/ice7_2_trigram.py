import nltk
from nltk.collocations import ngrams
from nltk.tokenize import word_tokenize
infile = open('input.txt','r', encoding="utf-8")
text = infile.read();
words = word_tokenize(text)
X = ngrams(words , 3)
for a in X:
    print(a)