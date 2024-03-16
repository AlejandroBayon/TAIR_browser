from urllib.request import urlopen
import time

time1 = time.perf_counter()

print("Obtaining HTML")

page = urlopen("https://www.arabidopsis.org/servlets/TairObject?id=6534023021&type=germplasm")
html_bytes = page.read()
html = html_bytes.decode("utf-8")

file = open("Prueba.txt", "w")
file.write(html)
file.close()

time2 = time.perf_counter()

total_time = time2 - time1

print(total_time)

#url1 = http://olympus.realpython.org/profiles/aphrodite
#url2 = https://www.arabidopsis.org/servlets/TairObject?id=6534023021&type=germplasm