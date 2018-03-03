from bs4 import BeautifulSoup
import urllib.request
url = "https://en.wikipedia.org/wiki/Python"
source_code = urllib.request.urlopen(url)
plain_text = source_code
soup = BeautifulSoup(plain_text, "html.parser")
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
fh = open('input.txt', 'w', encoding="utf-8")
text = '\n'.join(chunk for chunk in chunks if chunk)
fh.write(text)
fh.close()
print(text)
