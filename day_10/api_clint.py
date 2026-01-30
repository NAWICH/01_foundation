#use open-meteo api add latitude and logitude for kathmandu and set current_weather = true
#should return temperature, windspeed, weather_code
#make sure to use tyr/except to handle errors
#add fetch_quote() to return quote text and author
#add fetch_news(country) should get api from .env make a get request, parse json reponse extract top 5 headlines with title,source, url should return list of idctionaries
#add fetch_exchange_rates(base_currency) 
#add fetch_joke() should handle both single-part and two-part joke

import pandas as pd
from dotenv import load_dotenv
import os
import requests

def fetch_weather(city):
    load_dotenv()
    url = os.getenv('open-mateo_url')
    if city == 'kathmandu':
        latitude = 27.7017
        longitude = 85.3206
    elif city == 'pokhara':
        latitude = 28.2669
        longitude = 83.9685
    elif city == 'baglung':
        latitude = 28.2669
        longitude = 83.6663
    elif city == 'lalitpur':
        latitude = 28.2669
        longitude = 83.9685
    
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

def fetch_quote():
    load_dotenv()
    API_KEY = os.getenv('quotes')

    symbol = 'AAPL'
    url = "https://api.api-ninjas.com/v2/randomquotes".format(symbol)

    try:
        response = requests.get(url,headers={'X-Api-Key': API_KEY})
        quote_data = response.json()

        quote = {quote_data[0]['quote'], quote_data[0]['author']}

        return quote
    except Exception as e:
        print(f"The error is : {e}")

def fetch_news():
    try:
        load_dotenv()
        url = os.getenv('news_api')
        responses = requests.get(url)
        data = responses.json()
        if data['totalResults'] == 0:
            return None
        else:
            return data
    except Exception as e:
        print(e)

def fetch_exchange_rates(base_currency):
    try:
        load_dotenv()
        api_key = os.getenv('exchage_rate_api')

        url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/USD"

        reponses = requests.get(url)
        data = reponses.json()

        return data
    except Exception as e:
        print(f"Error is {e}")

def fetch_joke():
    try:
        load_dotenv()
        url = os.getenv('joke_api')

        responses = requests.get(url)
        print(responses)
        data = responses.json()

        if 'joke' in data:
            return {data['joke']}
        elif 'setup' in data and 'delivery' in  data:
            return {data['setup'], data['delivery']}
        else: 
            return None
    except Exception as e:
        print(f"The error is {e}")

