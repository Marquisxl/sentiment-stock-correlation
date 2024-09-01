import requests
from dotenv import load_dotenv
import os

# 環境変数の読み込み
load_dotenv()

API_KEY = os.getenv('NEWS_API_KEY')
query = 'technology'
url = f'https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}'

response = requests.get(url)
articles = response.json().get('articles', [])

for article in articles:
    print(f"Title: {article['title']}")
    print(f"Description: {article['description']}\n")