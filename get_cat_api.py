# A simple fetch API
import requests

#const
URL = "https://catfact.ninja/fact"

def get_cat_fact():
    try:
        response = requests.get(URL)
        if response.status_code == "200":
            return response
    except requests.RequestException as e:
        print(f"There was an error: {e}")
    return response

data = get_cat_fact().json()

print(f"Fact: {data.get('fact')}")

