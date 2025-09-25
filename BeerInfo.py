import requests 
import json
import pprint


# Base API = https://punkapi.online/v3/
# Random beer = beers/random
# Beer by ID = beers/{id}
# All beers by page (14 pages, 30 per page) = beers?page={page_number}
# Image of beer by id = images/{id}.png

# Optional parameters for /beer
# per_page = specify the number of items to return per page, the value can range from 10 to 80, 30 by default
# beer_name={string} =  retrieve a list of beers that match the specified string
# abv_gt={number} = retrieve a list of beers that have an ABV greater than the specified number
# abv_lt={number} = retrieve a list of beers that have an ABV less than the specified number
def get_all_beers():
    beer_list = [] # empty list to append dictionaries to

    for page in range(1,3): # may increase to all beers in database 

        url = f'https://punkapi.online/v3/beers?page={page}&per_page=30' # API Call 
        response = requests.get(url).json()

        # JSON response returns a list of dicts corresponding to each beer
        # for beer (every dictionary) in the json response
        # create a new dictionary with specified data
        # append every beer dictionary to a beer list for further processing
        for beer in response:
            beer_data = {
                "number":beer["id"],
                "name": beer["name"],
                "tag": beer["tagline"],
                "content": beer["abv"],
                "ibus": beer["ibu"],
                "first_brewed": beer["first_brewed"]
            }
            beer_list.append(beer_data)

    return beer_list




def get_beer_id(beerName):
    beer_list = []
    for page in range(1,6):
        url = f'https://punkapi.online/v3/beers?page={page}&per_page=30' # API Call 
        response = requests.get(url).json()
        for beer in response:
            beer_data = {
                "number":beer["id"],
                "name": beer["name"],
            }
            beer_list.append(beer_data)

    for beers in beer_list:
        if beerName.lower() in beers["name"].lower():
            return beers["number"]




