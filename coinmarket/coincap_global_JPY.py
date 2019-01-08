import json
import requests
from datetime import datetime

currency = 'JPY'

global_url = "https://api.coinmarketcap.com/v2/global/?convert=" + currency
# global_url = "https://pro.coinmarketcap.com/migrate/"

requests = requests.get(global_url)
results = requests.json()
# print(json.dumps(results,sort_keys=True, indent=4))


active_currencies = results['data']['active_cryptocurrencies']
print(active_currencies)

active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = int(results['data']['quotes'][currency]['total_market_cap'])
global_volume = int(results['data']['quotes'][currency]['total_volume_24h'])

active_currencies_string = '{:,}'.format(active_currencies)
active_markets_string = '{:,}'.format(active_markets)
global_cap_string = '{:,}'.format(global_cap)
global_volume_string = '{:,}'.format(global_volume)

last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d , %Y at %I:%M%p')

print()
print('There are currently ' + str(active_currencies) + ' active_cryptocurrencies and ' + str(active_markets) + ' active_markets.')
print('The global cap of all cryptos is ' + str(global_cap) + ' and the 24h global volume is ' + str(global_volume) + '. ')
print('Bitcoin \'s total percentage of the global cap is ' + str(bitcoin_percentage) + '. ')
print()
print('This information was last updated ' + str(last_updated) + '.' )


print()
print('There are currently ' + active_currencies_string + ' active_cryptocurrencies and ' + active_markets_string + ' active_markets.')
print('The global cap of all cryptos is ' + global_cap_string + ' and the 24h global volume is ' + global_volume_string+ '. ')
print('Bitcoin \'s total percentage of the global cap is ' + str(bitcoin_percentage) + '. ')
print()
print('This information was last updated ' + last_updated_string + '.' )

print(last_updated_string)
