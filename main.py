import requests

url = "http://secureaweb.fr"

reponse = requests.get(url)

print("URL :", url)
print("Status code :", reponse.status_code)
