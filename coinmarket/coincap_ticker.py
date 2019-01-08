import json
import requests

ticker_url = "https://api.coinmarketcap.com/v2/ticker/?structure=array"

limit = 100
start = 1
sort = 'id'
convert = 'USD'

choice = input("Do you want to enter any custom parameters?(y/n): ")
choice = str(choice)

if choice == 'y':
    limit = input('What is the custome limit ? : ')
    start = input('What is the custom start number ? : ')
    sort = input('What do you want to sort by ? : ')
    convert = input('What is your local currency?: ')

ticker_url += '&limit=' + limit + '&sort=' + sort + '&start=' + start + '&convert=' + convert

requests = requests.get(ticker_url)
results = requests.json()

print(json.dumps(results,sort_keys=True, indent=4))
