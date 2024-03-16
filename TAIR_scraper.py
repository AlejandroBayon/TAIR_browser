import requests

response = requests.get("https://www.arabidopsis.org/servlets/TairObject?id=6534023021&type=germplasm")

print(response.request.url)
print(response.request.body)
print(response)

file = open("prueba.txt", "w")

file.write(response.text)

file.close()