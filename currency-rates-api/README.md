# Currency Exchange Rate Tracker
This is a super beginner Python project that fetches real-time currency exchange rates using the free [Frankfurter API](https://www.frankfurter.app/). It runs in Google Colab and saves the data to a CSV file using `pandas`.

## Features
- Uses a public API (no API key required)
- Fetches all currencies relative to USD
- Saves rates and timestamps to CSV
- Outputs data to a pandas DataFrame

## How to Run
1. Open the `currency_rates_colab.ipynb` notebook in Google Colab
2. Run all cells
3. Download the CSV or save it to Google Drive

## Sample Output
1 USD = 0.92 EUR
1 USD = 0.79 GBP
1 USD = 157.5 JPY
…

## Dependencies
- `requests`
- `pandas`

Built by Saeid Torabi with ❤️ as a personal project to learn APIs, data collection, and data handling to use in further analysis.