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
