import re

file = open("html_page.html", "r")

count = 0

for line in file:
    id = re.search(r"id=(..........)&type=germplasm", line)
    if id:
        print(id.group(1))
        count += 1

print(count)