import requests
from geopy.geocoders import Nominatim

#geolocator = Nominatim(user_agent="maxin sää")
city = input("anna paikkakunnan nimi?: ")
#location = geocode(city)
#print(location.adress)

weather = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&lang=fi&APPID=7c449d15551f18e130e9229fa2887cc3"
request = requests.get(weather).json()
#print(request)

temperature = request["main"]
celsius = temperature["temp"]
final_temp = int(celsius) - 273.15
desc_weather = request["weather"]
desc2 = desc_weather[0]["description"]






print(F"paikkakunta {city} sää on {desc2} ja lämpötila {round(final_temp, 4)}c")