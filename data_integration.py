import requests
import json
from textblob import TextBlob
from dotenv import load_dotenv
import os

# 環境変数の読み込み
load_dotenv()

# NewsAPIからニュースデータを取得し、センチメント分析を行う
API_KEY = os.getenv('NEWS_API_KEY')
query = 'technology'  # 検索クエリとして使用するキーワード
url = f'https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}'
news_response = requests.get(url)
articles = news_response.json().get('articles', [])

news_data = []
for article in articles:
    # ニュース記事の感情スコアを計算
    sentiment = TextBlob(article['description']).sentiment.polarity
    news_data.append({
        'date': article['publishedAt'][:10],  # ISO形式の日付のうち、日付部分のみを使用
        'title': article['title'],            # 記事のタイトル
        'sentiment': sentiment                 # 記事のセンチメントスコア
    })

# Alpha VantageからAppleの株価データを取得
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
symbol = 'AAPL'  # Appleの株式シンボル
stock_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
stock_response = requests.get(stock_url)
stock_data = stock_response.json().get('Time Series (Daily)', {})

stock_prices = []
for date, values in stock_data.items():
    # 株価のオープン、高値、安値、クローズ値を取得して保存
    stock_prices.append({
        'date': date,
        'open': float(values['1. open']),
        'high': float(values['2. high']),
        'low': float(values['3. low']),
        'close': float(values['4. close'])
    })

# ニュースデータと株価データを日付でマッチングさせて結合する
combined_data = []
for news in news_data:
    for stock in stock_prices:
        if news['date'] == stock['date']:
            combined_data.append({
                'date': news['date'],
                'title': news['title'],
                'sentiment': news['sentiment'],
                'open': stock['open'],
                'high': stock['high'],
                'low': stock['low'],
                'close': stock['close']
            })

# 結合されたデータをJSONファイルとして保存する
with open('combined_data.json', 'w') as f:
    json.dump(combined_data, f, indent=4)  # indent=4を追加して、JSONファイルを読みやすく整形