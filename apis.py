import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
URL = "https://api.nasa.gov/planetary/apod?api_key=HbYkzkYIywGwqCOXAox9q0p3JtnPk6m3eZmnE7bW"
print("NASA_API_KEY:", os.getenv("NASA_API_KEY"))

def apod_generator(url, api_key):
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

apod_data = apod_generator(URL, NASA_API_KEY)

print(apod_data["title"])
print(apod_data["hdurl"])
print(apod_data["date"])
print(apod_data["explanation"])