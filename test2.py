import requests
import sys

sys.stdout.reconfigure(encoding = 'utf-8')

response = requests.get("https://countries.dev/countries")
print(response.status_code)

#data = response.json()
#print(data)