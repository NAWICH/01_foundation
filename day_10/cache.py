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
from api_clint import APIClient
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
        try:
            with open(self.cache_dir, 'r') as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return None

        if data is None or key not in data:
            return None
        
        #change str time to datetime.datetime format
        saved_time = datetime.strptime(data[key]['timestamp'], "%Y-%m-%d %H:%M:%S.%f")
        
        #calculate elapsed time and check if still valid
        elapsed = datetime.now() - saved_time
        if elapsed < self.cache_duration:
            return data[key]['data']  # Still valid
        else:
            print(f"Cache expired for {key}")
            return None  # Expired
        

    def set(self, key, data):
        # Read existing cache file
        try:
            with open(self.cache_dir, "r") as f:
                json_file = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            json_file = {}
        
        # Update/add the key with data and current timestamp (convert datetime to string)
        json_file.update({key:{
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            "data": data}
        })

        # Write everything back to cache file
        with open(self.cache_dir, "w") as f:
            json.dump(json_file, f, indent=4)


    def clear(self):
        with open(self.cache_dir, "w") as f:
            pass

