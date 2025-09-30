import requests 
import json
import pprint

class Beer():
    def __init__(self):
        self._beers = None
        self._hops = {}

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

    def get_all_beers(self):
        if self._beers is not None:
            return self._beers
        beer_list = [] # empty list to append dictionaries to

        for page in range(1,30): 

            url = f'https://punkapi.online/v3/beers?page={page}&per_page=30' # API Call 
            response = requests.get(url).json()

            # JSON response returns a list of dicts corresponding to each beer
            # for beer (every dictionary) in the json response
            # create a new dictionary with specified data
            # append every beer dictionary to a beer list for further processing
            for beer in response:
                beer_data = {
                    "id":beer["id"],
                    "name": beer["name"],
                    "tagline": beer["tagline"],
                    "abv": beer["abv"],
                    "ibu": beer["ibu"],
                    "first_brewed": beer["first_brewed"]
                }
                beer_list.append(beer_data)
        self._beers = beer_list
        return self._beers

    def get_beer_id(self, beerName):
        all_beer = self.get_all_beers()
        for beer in all_beer:
            if beerName.lower() in beer["name"].lower():
                return beer["id"]
            


    def get_hops_list(self, beerName):
        if beerName in self._hops:
            return self._hops[beerName]

        beerID = self.get_beer_id(beerName)
        url = f"https://punkapi.online/v3/beers/{beerID}"
        response = requests.get(url).json()

        if isinstance(response, list):
            beer = response[0]
        else:
            beer = response

        hops = beer.get("ingredients",{}).get("hops",[])

        hop_dict = {}
        for val in hops:
            hop_type = val["name"]
            attribute = val["attribute"]

            if hop_type not in hop_dict:
                hop_dict[hop_type] = {"Hop Type": hop_type, "Attributes": []}
            if attribute not in hop_dict[hop_type]["Attributes"]:
                hop_dict[hop_type]["Attributes"].append(attribute)

        hop_list = list(hop_dict.values())
        self._hops[beerName] = hop_list
        return hop_list

    
    def print_info(self, name):
        all_beers = self.get_all_beers()

        for beer in all_beers:
            if name.lower() in beer["name"].lower():
                hops_list = self.get_hops_list(name)
                hop_names = [hop["Hop Type"] for hop in hops_list]

                print(f'{beer.get("name")} is a(n) {beer.get("tagline")}. It\'s alcohol content is {beer.get("abv")}%.'
                      f'\nIt was first brewed on {beer.get("first_brewed")}. It contains the following hops: {", ".join(hop_names)}')
                return


    
    # def get_all_hops(self):
    #     all_beers = self.get_all_beers()
    #     hops_records = {}

    #     for beer in all_beers:
    #         name = beer["name"]
    #         hops = []

    #         if "ingredients" in beer and "hops" in beer["ingredients"]:
    #             for val in beer["ingredients"]["hops"]:
    #                 hop_type = val["name"]
    #                 attribute = val["attribute"]

    #                 if not any(h["Hop Type"] == hop_type for h in hops):
    #                     hops.append({"Hop Type": hop_type, "Attributes": [attribute]})
    #                 else:
    #                     for h in hops:
    #                         if h["Hop Type"] == hop_type and attribute not in h["Attributes"]:
    #                             h["Attributes"].append(attribute)

    #         hops_records[name] = hops

    #     return hops_records