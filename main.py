import os
from dotenv import load_dotenv
from weather_app import OpenWeatherMap

load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

if __name__ == "__main__":
    ### How to use it:
    city = input("Enter city name to get weather: ")
    # 1. Standard initialization (Instance)
    weather_client = OpenWeatherMap(api_key=OPENWEATHER_API_KEY)
    data = weather_client.get_weather(city)
    print(data)

    # 2. Using the Utility (Static)
    temp_c = float(input("Enter temperature in Celsius: "))
    temp_f = OpenWeatherMap.celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C is {temp_f}°F")