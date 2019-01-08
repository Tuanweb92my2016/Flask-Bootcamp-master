import json
import requests
from datetime import datetime


global_url = "https://api.coinmarketcap.com/v2/listings/"

requests = requests.get(global_url)
results = requests.json()

# print(json.dumps(results,sort_keys=True, indent=4))

data = results['data']

for currency in data:
    rank = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    print(str(rank) + ': ' + ' (' + symbol + ') ' )    
