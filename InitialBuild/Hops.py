# Gets the list of hops for a beer
import requests
import json
import pprint
from InitialBuild.BeerInfo import get_beer_id


beerName = "Old World India Pale Ale"

url = f"https://punkapi.online/v3/beers/{get_beer_id(beerName)}"
response = requests.get(url).json()

if isinstance(response, list):
    beer = response[0]
else:
    beer = response

hops = beer["ingredients"]["hops"]

hop_dict = {}
for val in hops:
    hop_type = val["name"]
    attribute = val["attribute"]

    if hop_type not in hop_dict:
        hop_dict[hop_type] = {"Hop Type": hop_type, "Attributes": []}

    if attribute not in hop_dict[hop_type]["Attributes"]:
        hop_dict[hop_type]["Attributes"].append(attribute)

hop_list = list(hop_dict.values())


pprint.pp(hop_list)

