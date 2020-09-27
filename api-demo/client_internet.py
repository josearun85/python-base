# Client code
import requests
import json

print("this is my client")

city = "Philadelphia"

url = "http://40.87.97.50:5001/geocode"

body = {"query" : city}
print(body)
my_req = requests.post(url, json=body)
response = json.loads(my_req.content)
print(response)
