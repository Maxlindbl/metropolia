import requests

request = "https://api.chucknorris.io/jokes/random?"
joke = requests.get(request).json()
#print(joke)
print(joke["value"])