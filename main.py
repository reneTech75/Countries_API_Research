#this is the main application. other modules will be called from her.
import requests
import sys

sys.stdout.reconfigure(encoding = 'utf-8') #this ensures that the terminal will print Arabic, Asian, and emoji characters.

#url = "https://countries.dev/countries"

#this function collects the inputs from the user at the terminal
def get_user_inputs():
    country = input("Please enter the name of the country you are researching:\n").strip().lower() 

    return {"country": country}

def fetch_data(user_input):

    params = {
        "name": user_input["country"]
    }
    url = "https://countries.dev/countries"
    response = requests.get(url, params = params)
    if response.status_code == 200:
        data = response.json()
        return data
    return {"error": f"data for {user_input['country']} could not be located"}
    
    




def main():
    user_input = get_user_inputs() #get the inputs from the user
    data = fetch_data(user_input) #get relevant records from the API provider
    print(data)


if __name__ == "__main__":
    main()
