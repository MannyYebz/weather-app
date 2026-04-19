import requests
from dotenv import load_dotenv
import os

class OpenWeatherMap:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key, units="metric"):
        self.api_key = api_key
        self.units = units

    def get_weather(self, city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": self.units
        }
        response = requests.get(self.BASE_URL, params=params, timeout=30)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"City {city} not found or API issue."}

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

def main():
    # looks for .env in whatever directory the user runs the command from
    load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        api_key = input("Enter your OpenWeatherMap API key: ")
        save = input("Save API key for future use? (y/n): ")
        if save.lower() == "y":
            with open(".env", "w") as f:
                f.write(f"OPENWEATHER_API_KEY={api_key}\n")
            print("✅ API key saved to .env")

    city = input("Enter city name to get weather: ")
    client = OpenWeatherMap(api_key=api_key)
    data = client.get_weather(city)

    if "error" in data:
        print(data["error"])
    else:
        temp_c = data['main']['temp']
        temp_f = client.celsius_to_fahrenheit(temp_c)
        print(f"\n🌤️ Weather in {city}:")
        print(f"  Temperature : {temp_c}°C / {temp_f:.1f}°F")
        print(f"  Feels like  : {data['main']['feels_like']}°C")
        print(f"  Condition   : {data['weather'][0]['description']}")
        print(f"  Humidity    : {data['main']['humidity']}%")

if __name__ == "__main__":
    main()