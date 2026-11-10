import requests
import json

response = requests.get("https://countries.dev/countries")

data = response.json()

for item in data:
    if item["name"].lower() == "cameroon":
        infor = json.dumps(item, ensure_ascii=True, indent=2)
        print(infor)


# json.dumps ensures characters are safely converted to text formatting your terminal can display
# clean_string = json.dumps(response.json(), ensure_ascii=True, indent=2)
# print(clean_string)