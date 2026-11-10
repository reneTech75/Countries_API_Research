#this is the main application. other modules will be called from her.
import requests
import sys

sys.stdout.reconfigure(encoding = 'utf-8') #this ensures that the terminal will print Arabic, Asian, and emoji characters.

url = "https://countries.dev/countries"

#this function collects the inputs from the user at the terminal
def get_user_inputs():
    country = input("Please enter the name of the country:\n").lower() 
    language = input("Please enter a language:\n").lower()
    density = float(input("please enter the desired population density:\n"))

    return {"country": country,
            "language": language,
            "population_density": density
           }

def fetch_data(user_inputs):
    response = requests.get(url)
    print(response)




def main():
    user_inputs = get_user_inputs() #get the inputs from the user
    fetch_data(user_inputs) #get relevant records from the API provider


if __name__ == "__main__":
    main()
