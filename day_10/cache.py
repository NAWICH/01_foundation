#crate a class called Cachemanager
#constructor(__init__):
    #cache_dir(where to store cache.defaule:"data")
    #duration_minutes(how long cache is valid)
    #what should this file do is:
        #create tje cache directory if it doesn't exist
        #store the duratiopn as a timedelta object
#method: get(key)
    #input a string key
    #check if cache file exists -> if not return NONE
    #read the cache file
    #check if the key exists in the cache -> return none if not
    #get the timestamp when 
    #calculate if it's been less than 60 minutes : return cached data else none

#method: set(key, data)
#key(string) and data (dictionary)
    #read existing cache file
    #add/update the key with: data & current timestamp
    #write everything back to cache file
#method: clear()
    #delete the cache file print confirmation message
from api_clint import fetch_exchange_rates, fetch_joke, fetch_news, fetch_quote, fetch_weather
import os
from datetime import timedelta, datetime
import json


class Cachemanager:
    def __init__(self, cache_dir, cache_duration):
        self.cache_dir = cache_dir
        self.cache_duration = cache_duration
        #if cache.json doesn't exsits create a new file
        if not os.path.exists(self.cache_dir):
            with open(self.cache_dir, "w") as f:
                pass
    
    def get(self, key):
        if not os.path.exists(self.cache_dir):
            return None
        
        #load json data
        with open(self.cache_dir, 'r') as f:
            data = json.load(f)

        if key not in data:
            return None
        #change str time to datetime.datetime format
        saved_time = datetime.strptime(data[key]['timestamp'], "%Y-%m-%d %H:%M:%S.%f")
        
        #return data if it is fresh else return none
        if self.cache_duration - saved_time < timedelta(minutes=60):
            return None
        else:
            return data
        

    def set(self, key, data):
        # Read existing cache file
        try:
            with open(self.cache_dir, "r") as f:
                json_file = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            json_file = {}
        
        # Update/add the key with data and current timestamp (convert datetime to string)
        json_file.update({
            "timestamp": self.cache_duration.strftime("%Y-%m-%d %H:%M:%S.%f"),
            "data": data
        })

        # Write everything back to cache file
        with open(self.cache_dir, "w") as f:
            json.dump(json_file, f, indent=4)


    def clear(self):
        with open(self.cache_dir, "w") as f:
            pass
now = datetime.now()
duration = now + timedelta()
d = Cachemanager("cache.json", duration)
d.clear()