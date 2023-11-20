import requests

try:
    request = "https://api.chucknorris.io/jokes/random"
    joke = requests.get(request).json()
    print(joke["value"])
except requests.exceptions.RequestException as e:
    print("Request Error")
    
