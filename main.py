#this is the main application. other modules will be called from her.
import requests
from urllib.parse import quote #we need this because the names of some countries haves spaces
import sys

sys.stdout.reconfigure(encoding = 'utf-8') #this ensures that the terminal will print Arabic, Asian, and emoji characters.

#url = "https://countries.dev/countries"

#this function collects the inputs from the user at the terminal
def get_user_inputs():
    country = input("Please enter the name of the country you are researching:\n").strip().lower() 

    return {"country": country}

def fetch_data(user_input):

    country = user_input["country"]

    # Encode the country name for use in a URL
    url = f"https://countries.dev/name/{quote(country, safe='')}"

    try:
        response = requests.get(url, timeout=10) # we wait for a response no longer than 10s

        if response.status_code == 200:
            data = response.json()
            for record in data:
                if record["name"].lower() == country:
                    return record
            return {"error": f"No exact match found for {country}"}
            

        elif response.status_code == 404:
            return {"error": f"Country {country} could not be located"}
            
        else:
            return {"error": f"API request failed: {response.status_code}"}
        

    except requests.exceptions.Timeout:
        return {"error": "The API request timed out"}

    except requests.exceptions.RequestException as error:
        return {"error": f"Connection error: {error}"}

def get_summary(metrics):
    return f"{metrics['country']} is a country in {metrics['region']}, with a population of {metrics['population']}. It has {len(metrics['languages'])} official language(s)"
    




def main():
    user_input = get_user_inputs() #get the inputs from the user
    data = fetch_data(user_input) #get relevant records from the API provider
    print(data)
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
