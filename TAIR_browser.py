import requests

response = requests.get("https://www.arabidopsis.org/servlets/")

print(response.request.url)
print(response.request.body)
print(response)