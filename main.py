#this is the main application. other modules will be called from her.
import requests

base_url = "https://countries.dev/countries"

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
    url = f"{base_url}/{id}"
    response = requests.get(url)




def main():
    user_inputs = get_user_inputs()
    fetch_data(user_inputs)


if __name__ == "__main__":
    main()
