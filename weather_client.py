import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "7c6d9f16cc55e9b5efc85c65a4664696"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)

Joke_URL = "https://official-joke-api.appspot.com/random_joke"

def get_joke():
	res = requests.get(Joke_URL)
	return res.json()
	

def main():
    temp = get_weather("London")
    print(temp)
    joke = get_joke()
    print(joke)

if __name__ == "__main__":
    main()
