import nltk
from nltk.tokenize import word_tokenize , wordpunct_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
infile = open('input.txt','r', encoding="utf-8")
text = infile.read();
words = word_tokenize(text)
ps = PorterStemmer()
for w in words:
   print(ps.stem(w))