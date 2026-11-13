#this is the main application. other modules will be called from her.
import requests
from urllib.parse import quote #we need this because the names of some countries haves spaces
import sys

sys.stdout.reconfigure(encoding = 'utf-8') #this ensures that the terminal will print Arabic, Asian, and emoji characters.

#url = "https://countries.dev/countries"

#this function collects the inputs from the user at the terminal. The program stops if nothing is entered
def get_user_inputs() -> dict:
    country = input("Please enter the name of the country you are researching:\n").strip().lower() 
    if country == "":
        print("You did not enter the name of any country. ")
        sys.exit("The program will stop now, come back when you have the name of a country!!!")
    return {"country": country}

#this function fetches the record of the country of interest
def fetch_data(user_input: dict) -> list | dict:
    country = user_input["country"]

    # Encode the country name in a URL, this API provider doesn't accept query parameters
    url = f"https://countries.dev/name/{quote(country, safe='')}"

    try:
        response = requests.get(url, timeout=10) # we wait for a response no longer than 10s

        if response.status_code == 200:
            data = response.json()
            for record in data: #this loop is needed since we may get partial matchings(eg "united" will bring many results like united Arab Emirates, United Kingdon, united states), and thus need to filter the exact country
                if record["name"].lower() == country:
                    return record
            return {"error": f"No exact match found for {country}"}
            
        elif response.status_code == 404:
            return {"error": f"The country: {country}, could not be located"}
            
        else:
            return {"error": f"API request failed: {response.status_code}"}
        
    except requests.exceptions.Timeout:
        return {"error": "The API request timed out"}

    except requests.exceptions.RequestException as error:
        return {"error": f"Connection error: {error}"}

def get_summary(metrics: dict) -> str:
    return f"{metrics['country']} is a country in {metrics['region']}, with a population of {metrics['population']}. It has {len(metrics['languages'])} official language(s)"
    
#this main function will direct the main logic flow of this program.
def main() -> None:
    user_input = get_user_inputs() #get the inputs from the user
    data = fetch_data(user_input) #get relevant records from the API provider
    try:# this try block succeeds only when the response object has a payload
        name = user_input["country"]
        region = data["region"]
        capital = data["capital"]
        population = data["population"]
        languages = data["languages"]
 
        metrics = {
            "country": name,
            "region": region,
            "capital": capital,
            "population": population,
            "languages": languages
           }
        summary = get_summary(metrics)
        print(summary)
    except:
        print(data["error"])

if __name__ == "__main__":
    main()
