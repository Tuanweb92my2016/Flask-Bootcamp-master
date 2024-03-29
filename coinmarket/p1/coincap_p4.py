import math
import locale
import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

global_url = 'https://api.coinmarketcap.com/v2/global/'
ticker_url = 'https://api.coinmarketcap.com/v2/ticker/?structure=array'


request = requests.get(global_url)
results = request.json()
data = results['data']
global_cap = int(data['quotes']['USD']['total_market_cap'])

table = PrettyTable(['Name','Ticker','% of total global cap','Content','7.7T (Gold)','36.6T (Narrow Money)','73T ( World Stock Markets)','90.4T ( Broad Money)','217T (Real Estate)','544T (Derivatives)'])

request = requests.get(ticker_url)
results = request.json()
data = results['data']

for currency in data:
    name = currency['name']
    ticker = currency['symbol']
    percentage_of_global_cap = float(currency['quotes']['USD']['market_cap'])/float(global_cap)

    currency_price = round(float(currency['quotes']['USD']['price']),2)
    available_supply = float(currency['total_supply'])

    trillion7price = round(77000000000000 * percentage_of_global_cap / available_supply,2)
    trillion36price = round(360000000000000 * percentage_of_global_cap / available_supply,2)
    trillion73price = round(730000000000000 * percentage_of_global_cap / available_supply,2)
    trillion90price = round(900000000000000 * percentage_of_global_cap / available_supply,2)
    trillion217price = round(217000000000000 * percentage_of_global_cap / available_supply,2)
    trillion544price = round(544000000000000 * percentage_of_global_cap / available_supply,2)

    percentage_of_global_cap_string = str(round(percentage_of_global_cap*100,2)) + '%'
    current_price_string = '$' + str(currency_price)
    trillion7price_string = '$'+ locale.format('%.2f',trillion7price,True)
    trillion36price_string = '$'+ locale.format('%.2f',trillion36price,True)
    trillion73price_string = '$'+ locale.format('%.2f',trillion73price,True)
    trillion90price_string = '$'+ locale.format('%.2f',trillion90price,True)
    trillion217price_string = '$'+ locale.format('%.2f',trillion217price,True)
    trillion544price_string = '$'+ locale.format('%.2f',trillion544price,True)

    table.add_row([name,
                    ticker,
                    percentage_of_global_cap_string,
                    current_price_string,
                    trillion7price_string,
                    trillion36price_string,
                    trillion73price_string,
                    trillion90price_string,
                    trillion217price_string,
                    trillion544price_string])

print()
print(table)
print()
