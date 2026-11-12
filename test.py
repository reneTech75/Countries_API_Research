import requests
import sys

sys.stdout.reconfigure(encoding = 'utf-8')

country = "Cameroon"



response = requests.get(f"https://countries.dev/countries/name/{country}")
print(response.status_code)
data = response.json()
print(data)

<<<<<<< HEAD



# for item in data:
#     if item["name"].lower() == "cameroon":
#         infor = json.dumps(item, ensure_ascii=True, indent=2)
#         print(infor)
=======
for item in data:
    if item["name"].lower() == "usa":
        infor = json.dumps(item, ensure_ascii=True, indent=2)
        print(infor)
        print(item["region"])
>>>>>>> tests


# json.dumps ensures characters are safely converted to text formatting your terminal can display
# clean_string = json.dumps(response.json(), ensure_ascii=True, indent=2)
# print(clean_string)