#this is the main application. other modules will be called from her.
import requests
import sys

sys.stdout.reconfigure(encoding = 'utf-8') #this ensures that the terminal will print Arabic, Asian, and emoji characters.

url = "https://countries.dev/countries"

#this function collects the inputs from the user at the terminal
def get_user_inputs():
    country = input("Please enter the name of the country you are researching:\n").strip().lower() 

    return {"country": country}

def fetch_data(user_input):
    response = requests.get(url)
    all_data = response.json() #converts JSON string into python object
    for item in all_data:
        if item["name"].lower() == user_input["country"]:
            return item
    return "Unfortunately, there is no data on the country your provided"

def get_summary(metrics):
    return f"{metrics['country']} is a country in {metrics['region']}, with a population of {metrics['population']}. It has {len(metrics['languages'])} official language(s)"





def main():
    user_input = get_user_inputs() #get the inputs from the user
    data = fetch_data(user_input) #get relevant records from the API provider
    region = data["region"]
    capital = data["capital"]
    population = data["population"]
    languages = data["languages"]
    
    metrics = {
        "country": user_input["country"],
        "region": region,
        "capital": capital,
        "population": population,
        "languages": languages
    }

    summary = get_summary(metrics)
    
    
    #print(data)
    print(summary)


if __name__ == "__main__":
    main()
