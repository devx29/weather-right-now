from pprint import pprint
from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_weather_now(city="New York"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"
    weather_data = requests.get(request_url).json()
    return weather_data
    # pprint(weather_data)
    # print(f"Current temperature in {city.capitalize()} is {weather_data['main']['temp']:.2f} degrees farenheit")

if __name__ == "__main__":
    print("*******GET WEATHER NOW*******")
    city = input("\nEnter city name: ")

    if not bool(city.strip()):
        city = "New York"

    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"
    weather_data = requests.get(request_url).json()

    pprint(weather_data)