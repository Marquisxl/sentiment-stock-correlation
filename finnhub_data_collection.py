import requests
from dotenv import load_dotenv
import os

# 環境変数の読み込み
load_dotenv()

API_KEY = os.getenv('FINNHUB_API_KEY')
symbol = 'AAPL'
url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}'

response = requests.get(url)
data = response.json()

print(f"Current Price: {data['c']}")
print(f"High Price: {data['h']}")
print(f"Low Price: {data['l']}\n")