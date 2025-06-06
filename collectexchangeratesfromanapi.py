# -*- coding: utf-8 -*-
"""CollectExchangeRatesFromAnAPI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Voq6hj3O4emNW8QI-2uRll-7oZZGb1FI

# **Personal Project**
to practice collecting Exchange Rates Data from a free api and save it to a csv file. also we can convert it to a pandas df and use it later in our analysis :)
"""

import requests
import csv
import datetime
import pandas as pd

# just to get the currency codes from this link
def get_currency_codes():
  url='https://api.frankfurter.app/currencies'
  response = requests.get(url)
  data = response.json()
  return list(data.keys())

# to get the rates from the api
def get_currency_rates(base='USD', symbols=None):
  if symbols is None:
    symbols = get_currency_codes()
  symbols_str = ','.join(symbols)
  url = f'https://api.frankfurter.app/latest?from={base}&to={symbols_str}'
  response = requests.get(url)
  data = response.json()
  return data.get('rates', {}), data.get('date', '')

# to save the data as csv in colab
def save_to_csv(rates, date, filename='exchange_rates.csv'):
  now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Currency', 'Rate (1 USD = ...)', 'Date', 'Time Collected'])
    for currency, rate in rates.items():
      writer.writerow([currency, rate, date, now])

# to call the afformentioned functions and print the exchange rates
def main():
  print('Collecting data...')
  rates, date = get_currency_rates()
  for currency, rate in list(rates.items()):
    print(f'1 USD = {rate} {currency}')
  save_to_csv(rates, date)
  print("\nRates saved successfully to 'exchange_rates.csv'")

# the start button :)
if __name__ == '__main__':
  main()

# to download the file from colab to our compouter

from google.colab import files
files.download("exchange_rates.csv")

rates, date = get_currency_rates() # because it was local in the function before, we should do it again

# to convert rates dictionary to a pandas DataFrame
df = pd.DataFrame(rates.items(), columns=['Currency', 'Rate'])

# Add date and timestamp to the dataframe
df['Date'] = date
df['Collected_At'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

df

# saving to csv in pandas is much easier :)
df.to_csv('exchange_rates_pandas.csv', index=False)

# again to download to our computer
from google.colab import files
files.download("exchange_rates_pandas.csv")