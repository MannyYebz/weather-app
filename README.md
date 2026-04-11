# How to Install
# How to run
# How to integrate API_key

# Weather App 🌤️

A Python package for fetching real-time weather data using the OpenWeatherMap API.

## Installation

```bash
pip install weather-app-mannyyebz
```

## Setup

1. Get a free API key from [openweathermap.org](https://openweathermap.org)
2. Create a `.env` file in your project:



## Usage

```python
from weather_app import OpenWeatherMap

# Get weather for a city
client = OpenWeatherMap(api_key="your_api_key")
data = client.get_weather("New York")
print(data)

# Convert Celsius to Fahrenheit
temp_f = OpenWeatherMap.celsius_to_fahrenheit(25)
print(f"25°C is {temp_f}°F")
```

## Features

- Fetch real-time weather data for any city
- Returns temperature, humidity, wind speed, and more
- Built-in Celsius to Fahrenheit converter

## Dependencies

- `requests`
- `python-dotenv`

## License

MIT