import requests
# OpenWeatherAPI.cpm
from API import API_KEY # If the API key is in separate file (Best practice, recommended)

api = API_KEY  # API_KEY = 'Your API'  (enter your api key in the variable API_KEY in seperate file names as API.py, and add it

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric" # URL of site
# do not use http website (port 80)
    response4 = requests.get(url)
# name, temp, humidity, weather
    if response4.status_code == 200:
        data = response4.json()
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']} C")
        print(f"Humidity: {data['main']['humidity']} %")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")

    else:
        print("City Not Found or Something went wrong.")


City = input("Enter the city name: ")
get_weather(City)
