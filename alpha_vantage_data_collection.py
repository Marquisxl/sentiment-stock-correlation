import requests
from dotenv import load_dotenv
import os

# 環境変数の読み込み
load_dotenv()

API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
symbol = 'AAPL'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'

response = requests.get(url)
data = response.json()

time_series = data.get('Time Series (Daily)', {})

for date, values in time_series.items():
    print(f"Date: {date}")
    print(f"Open: {values['1. open']}")
    print(f"High: {values['2. high']}")
    print(f"Low: {values['3. low']}")
    print(f"Close: {values['4. close']}\n")