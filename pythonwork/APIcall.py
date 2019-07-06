import requests

r = requests.get("https://api.linkedin.com")
print(r.text)
print("_____________________")
print(r.json)
