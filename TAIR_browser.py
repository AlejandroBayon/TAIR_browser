import requests

response = requests.get("https://www.arabidopsis.org/servlets/TairObject?id=30616&type=locus")

print(response.request.url)
print(response.request.body)
print(response)

file = open("prueba.txt", "w")

file.write(response.text)

file.close()