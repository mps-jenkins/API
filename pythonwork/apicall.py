import json
import requests


api_key="151f93124453b163c9c6e4e5b94b29bac0a4d198"
base_url="https://api.github.com/users/mps-jenkins/repos?"
full_url= base_url + "appid=" + api_key

result = requests.get(full_url)
result1= json.dumps(result.text)
print(result1)
print(type(result1))