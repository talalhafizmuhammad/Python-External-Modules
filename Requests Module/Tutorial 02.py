"""
Title: Web Scraping, Parsing, and API Integration in Python

Description:
This script demonstrates:
1. Making HTTP requests using the 'requests' module.
2. Web scraping and parsing using 'BeautifulSoup'.
3. Interacting with public APIs (e.g., GitHub & OpenWeatherMap).
4. Extracting and displaying structured data like weather info and webpage metadata.

"""

import requests
url = 'https://github.com'
response = requests.get(url)

response1 = requests.get(url).content
print(response1)  # Web scraping: Extracting content from a website/webpage (in form of HTML) -->> raw form of data

# getting headers from a url
print(response1.headers)
print(response1.headers['Content-Type'])

# Customizing get requests

response2 = requests.get("https://api.github.com/search/repositories",
                        params = {'q': 'language: python', 'sort': 'stars' , 'order': 'asc'})

Resp = response2.json()

Repos = Resp['items']


# printing according to need
for i in Repos[:5]:
    print(f"Name: {i['name']}")
    print(f"Description: {i['description']}")
    print(f"Stars: {i['stargazers_count']}")

# Web Parsing: Extract data in organized format from a website/webpage (HTML)

from bs4 import BeautifulSoup    # Web parsing   (pip install beautifulsoup4)

url = 'https://google.com'
response3 = requests.get(url)
print(response3)  #status code: 200 ok

soup = BeautifulSoup(response3.text, 'html.parser')

print(f"Page title: {soup.title.text}")  #Extract page title of the URL


# Extract all links from a webpage
for i in soup.find_all('a'):
    print(f"Link: {i.get('href')}")


# Getting weather data from an OpenWeather site (API KEY)


# go to openweatherapi.com, sign in, and request API key

from API import API_KEY

api = API_KEY  # API_KEY = 'Your API'  (enter your api key in the variable API_KEY in seperate file names as API.py, and add it

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
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














