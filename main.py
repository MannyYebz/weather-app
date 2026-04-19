import os
from dotenv import load_dotenv
from weather_app import OpenWeatherMap

load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

if __name__ == "__main__":
    city = input("Enter city name to get weather: ")
    
    weather_client = OpenWeatherMap(api_key=OPENWEATHER_API_KEY)
    data = weather_client.get_weather(city)
    
    if "error" in data:
        print(data["error"])
    else:
        temp_c = data['main']['temp']
        temp_f = weather_client.celsius_to_fahrenheit(temp_c)
        print(f"\n🌤️ Weather in {city}:")
        print(f"  Temperature : {temp_c}°C / {temp_f:.1f}°F")
        print(f"  Feels like  : {data['main']['feels_like']}°C")
        print(f"  Condition   : {data['weather'][0]['description']}")
        print(f"  Humidity    : {data['main']['humidity']}%")