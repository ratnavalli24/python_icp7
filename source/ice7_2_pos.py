import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
infile = open('input.txt','r', encoding="utf-8")
text = infile.read();
words = word_tokenize(text)
print(pos_tag(words))