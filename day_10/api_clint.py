#use open-meteo api add latitude and logitude for kathmandu and set current_weather = true
#should return temperature, windspeed, weather_code
#make sure to use tyr/except to handle errors
#add fetch_quote() to return quote text and author
#add fetch_news(country) should get api from .env make a get request, parse json reponse extract top 5 headlines with title,source, url should return list of idctionaries
#add fetch_exchange_rates(base_currency) 
#add fetch_joke() should handle both single-part and two-part joke

from dotenv import load_dotenv
import os
import requests


class APIClient:
    def __init__(self):
        """Initialize the API client."""
        load_dotenv()
    
    def fetch_weather(self, city):
        """Fetch weather data for a given city."""
        url = os.getenv('open-mateo_url')
        
        city_coords = {
            'kathmandu': (27.7017, 85.3206),
            'pokhara': (28.2669, 83.9685),
            'baglung': (28.2669, 83.6663),
            'lalitpur': (28.2669, 83.9685)
        }
        
        if city.lower() not in city_coords:
            return {"error": f"City '{city}' not supported"}
        
        latitude, longitude = city_coords[city.lower()]
        
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": ["temperature_2m", "wind_speed_10m", "weather_code"],
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()
            return data
        except Exception as e:
            print(f"error is {e}")
            return None

    def fetch_quote(self):
        """Fetch a random quote."""
        API_KEY = os.getenv('quotes')

        url = "https://api.api-ninjas.com/v2/randomquotes"

        try:
            response = requests.get(url, headers={'X-Api-Key': API_KEY})
            quote_data = response.json()

            quote = {'quote': quote_data[0]['quote'], 'author': quote_data[0]['author']}
            return quote
        except Exception as e:
            print(f"The error is : {e}")
            return None

    def fetch_news(self, country='US'):
        """Fetch news headlines for a given country."""
        try:
            url = os.getenv('news_api')
            params = {'country': country}
            responses = requests.get(url, params=params)
            data = responses.json()
            
            if data.get('totalResults', 0) == 0:
                return None
            else:
                # Extract top 5 headlines
                articles = data.get('articles', [])[:5]
                headlines = []
                for article in articles:
                    headlines.append({
                        'title': article.get('title', ''),
                        'source': article.get('source', {}).get('name', ''),
                        'url': article.get('url', '')
                    })
                return headlines
        except Exception as e:
            print(e)
            return None

    def fetch_exchange_rates(self, base_currency):
        """Fetch exchange rates for a base currency."""
        try:
            api_key = os.getenv('exchage_rate_api')

            url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"

            responses = requests.get(url)
            data = responses.json()

            return data
        except Exception as e:
            print(f"Error is {e}")
            return None

    def fetch_joke(self):
        """Fetch a joke (handles single-part and two-part jokes)."""
        try:
            url = os.getenv('joke_api')

            responses = requests.get(url)
            data = responses.json()

            if 'joke' in data:
                return {'joke': data['joke']}
            elif 'setup' in data and 'delivery' in data:
                return {'setup': data['setup'], 'delivery': data['delivery']}
            else:
                return None
        except Exception as e:
            print(f"The error is {e}")
            return None

