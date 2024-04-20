from urllib.request import urlopen
import time
from bs4 import BeautifulSoup

time1 = time.perf_counter()

print("Obtaining HTML")

page = urlopen("https://www.arabidopsis.org/servlets/TairObject?id=6534023021&type=germplasm")
html = page.read().decode("utf-8")

file = open("HTML_text.txt", "w")
file.write(html)
file.close()

time2 = time.perf_counter()

total_time = time2 - time1
print(total_time)

soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()

file = open("clean_text.txt", "w")
file.write(text)
file.close()

#url1 = http://olympus.realpython.org/profiles/aphrodite
#url2 = https://www.arabidopsis.org/servlets/TairObject?id=6534023021&type=germplasm
#url3 = https://www.arabidopsis.org/servlets/TairObject?id=34504&type=locus
#url4 = https://www.arabidopsis.org/servlets/TairObject?id=503109900&type=polyallele