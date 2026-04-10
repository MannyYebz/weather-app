import requests

class OpenWeatherMap:
    # Class Attribute: The base URL for the API
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key, units="metric"):
        # Instance Attributes: Unique to each 'client' object
        self.api_key = api_key
        self.units = units

    # --- Instance Method ---
    def get_weather(self, city):
        """Fetches current weather for a specific city."""
        params = {
            "q": city,
            "appid": self.api_key,
            "units": self.units
        }
        response = requests.get(self.BASE_URL, params=params, timeout=30)  # Added timeout for better error handling
       
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"City {city} not found or API issue."}

    # --- Static Method ---
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Utility method: doesn't need 'self' or 'cls'."""
        return (celsius * 9/5) + 32
    