import requests
import json

convert = 'USD'

listing_url = 'https://api.coinmarketcap.com/v2/listings/'
url_end = '?structure=array&convert=' + convert

requests = requests.get(listing_url)
results = requests.json()

data = results['data']

ticker_url_pairs = {}
for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url

print(ticker_url_pairs)

while True:

    print()
    choice = raw_input("Enter the ticket symbol of a cryptocurrency: ")
    choice = choice.upper()

    ticker_url='https://api.coinmarketcap.com/v2/ticker/' + str(ticker_url_pairs[choice]) + '/' + url_end
    print(ticker_url)
    requests = requests.get(ticker_url)
    results = requests.json()

    print(json.dumps(results,sort_keys=True, indent=4))

    data = results['data'][0]
    
