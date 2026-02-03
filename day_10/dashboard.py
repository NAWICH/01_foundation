#main program
#imports:
    #APICLIENT
    #CacheManager
    #argparse
#fetchall_data(location, api_client, cache):
    #for each api:
        #check cache: if hit use cached data
        #if cache miss: call api client
        #save cache
    #return dictionary with all data

#display_data(data):
    #data = fetch_all_data()
    #if none print warning

#save_snapshot(data):
    #Create filename based on today's date (e.g., "2026-01-29.json")
    # Save to "data/" directory
    # Write data as formatted JSON (use indent=2)
    # Print confirmation message

#main:
    # Set up argument parser
    # Parse command-line arguments
    # Create instances of APIClient and CacheManager
    # If --clear-cache flag: clear cache and exit
    # Call fetch_all_data()
    # Call display_data()
    # Call save_snapshot()`

from api_clint import APIClient
from cache import Cachemanager
import argparse
import json
from datetime import datetime, timedelta
import os



def fetchall_data(location, api_client, cache):
    timestamp = datetime.now()
    result_dir = {
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"),
        "location" : location,
        "weather" : None,
        "joke" : None,
        "quote": None,
        "news": None,
        "exchange_rate": None
    }
    #getting the weather data
    weather_data = cache.get("weather")
    if weather_data is not None: 
        print("Using Cached weather....")
    else: 
        print("Fetching Weather from API")
        weather_data = api_client.fetch_weather(location)
        if weather_data is not None:
            cache.set("weather", weather_data)
    result_dir["weather"] = weather_data

    #getting the joke data
    joke_data = cache.get("joke")
    if joke_data is not None: 
        print("Using Cached Joke....")
    else: 
        print("Fetching Joke from API")
        joke_data = api_client.fetch_joke()
        if joke_data is not None:
            cache.set("joke", joke_data)
    result_dir["joke"] = joke_data


    #getting the quote
    quote_data = cache.get("quote")
    if quote_data is not None: 
        print("Using Cached quote....")
    else: 
        print("Fetching quote from API")
        quote_data = api_client.fetch_quote()
        if quote_data is not None:
            cache.set("quote", quote_data)
    result_dir["quote"] = quote_data

    #getting the news data
    news_data = cache.get("news")
    if news_data is not None: 
        print("Using Cached News....")
    else: 
        print("Fetching News from API")
        news_data = api_client.fetch_news()
        if news_data is not None:
            cache.set("news", news_data)
    result_dir["news"] = news_data

    #getting the exchange_rate data
    exchange_rate_data = cache.get("exchange_rate")
    if exchange_rate_data is not None: 
        print("Using Cached Exchange_rate....")
    else: 
        print("Fetching Exchange_rate from API")
        exchange_rate_data = api_client.fetch_exchange_rates("NPR")
        if exchange_rate_data is not None:
            cache.set("exchange_rate", exchange_rate_data)
    result_dir["exchange_rate"] = exchange_rate_data

    return result_dir

def display_data(data,location):
    '''ARG:
        data: the dicctionary from fetch_alldata()
        location: city name for display'''
    
    print("📊API DASHBOARD")
    print(f"Location: 🗺️{location}")
    print(f"current date and time : ⌚{datetime.now()}")
    print("----------------------------------------------------\n")

    #display wetehr section
    if data["weather"] is None:
        print("❌Weather data unavilabe")
    else:
        print("⛅WEATHER\n")
        print(f"Temperature: {data["weather"]["current"]["temperature_2m"]}℃\n")
        print(f"Wind Speed: {data["weather"]["current"]["wind_speed_10m"]}Km/h")
        print("----------------------------------------------------\n")

    #display quote
    if data["quote"] is None:
        print("❌quote is unavilabe")
    else:
        print("💭 QUOTE OF THE DAY:\n")
        print(f"{data['quote']['quote']}")
        print(f"author: {data['quote']['author']}")
        print("----------------------------------------------------\n")

    #display news
    if data["news"] is None:
        print("News is unavilabe right now")
    else: 
        print("📰TOP NEWS\n")
        for news in data['news']:
            print(f"Title: {news['title']}\n")
            print(f"source: {news['source']}\n")
            print(f"Link: {news['url']}\n")
        print("----------------------------------------------------\n")

    #display Exchange rate
    if data['exchange_rate'] is None:
        print("Exchange rate is unavilabe")
    else:
        print("💱 EXCHANGE RATES")
        print(f"{data['exchange_rate']["base_code"]} --> {data['exchange_rate']["target_code"]} : {data['exchange_rate']["conversion_rate"]}")
        print("----------------------------------------------------\n")

    #Display joke
    if data['joke'] is None:
        print("Joke unavilable")
    else:
        print("😁JOKE")
        if 'joke' in data['joke']:
            print(data['joke']['joke'])
        elif 'setup' in data['joke'] and 'delivery' in data['joke']:
            print(f"{data['joke']['setup']}\n{data['joke']['delivery']}")
        else:
            print("No joke found in this format.")

result = fetchall_data("kathmandu", APIClient(), Cachemanager("cache.json", timedelta(minutes=60)))
display_data(result, 'kathmandu')