import os
import json
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import openmeteo_requests
import requests_cache
from retry_requests import retry

def read_config():
    # Adjusted to your specific file path
    with open('day_9/config.json', 'r') as f:
        return json.load(f)

def get_weather_description(code):
    # Mapping for Open-Meteo WMO codes
    mapping = {
        0: "Clear sky",
        1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Depositing rime fog",
        51: "Light drizzle", 61: "Slight rain",
        71: "Slight snowfall", 95: "Thunderstorm"
    }
    return mapping.get(code, f"Unknown ({code})")

def main():
    # 1. Setup API client
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # 2. Load Config and Env
    load_dotenv()
    url = os.getenv('url')
    config = read_config()

    # 3. Get User Input
    cities = list(config["latitude"].keys())
    print("\nSelect a location:")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city.capitalize()}")
    
    try:
        choice_idx = int(input("Enter choice: ")) - 1
        selected_city = cities[choice_idx]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    # 4. Prepare API Parameters based on your JSON structure
    params = {
        "latitude": config["latitude"][selected_city],
        "longitude": config["longitude"][selected_city],
        "current": config["current"],
        "timezone": config["timezone"],
        "wind_speed_unit": config["wind_speed_unit"]
    }

    # 5. Fetch Data
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    current = response.Current()

    # 6. Extract Variables (Mapping indices to your 'current' list)
    # 0: temp, 1: humidity, 2: is_day, 3: rain... (matches config order)
    temp = current.Variables(0).Value()
    humidity = current.Variables(1).Value()
    # Note: If you want weather_code, you must add "weather_code" to your config['current'] list!
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 7. Create Output Data
    weather_data = {
        "timestamp": timestamp,
        "city": selected_city,
        "temperature_2m": f"{round(temp, 2)}°C",
        "relative_humidity_2m": f"{int(humidity)}%",
        "is_day": "Day" if current.Variables(2).Value() == 1 else "Night",
        "wind_speed": f"{round(current.Variables(6).Value(), 2)} m/s"
    }

    # 8. Save to unique file
    filename = f"{selected_city}_data.json"
    with open(filename, 'w') as f:
        json.dump(weather_data, f, indent=4)

    print(f"\n--- Results for {selected_city.capitalize()} ---")
    print(json.dumps(weather_data, indent=2))
    print(f"\nSaved to {filename}")

if __name__ == "__main__":
    main()