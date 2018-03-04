from nltk.tokenize import word_tokenize, wordpunct_tokenize
from nltk import pos_tag, ne_chunk
infile = open('input.txt','r', encoding="utf-8")
text = infile.read();
words = word_tokenize(text)
print(ne_chunk(pos_tag(words)))