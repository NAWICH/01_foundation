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