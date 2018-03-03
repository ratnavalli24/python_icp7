import nltk
nltk.download()
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
infile = open('input.txt','r', encoding="utf-8")
text = infile.read();
lem = WordNetLemmatizer()
words = word_tokenize(text)
for word in words:
  print(lem.lemmatize(word, pos='v'))

