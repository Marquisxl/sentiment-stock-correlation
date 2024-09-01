import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# JSONファイルからデータを読み込む
with open('combined_data.json', 'r') as f:
    combined_data = json.load(f)

# センチメントスコアと株価終値のリストを作成
sentiments = [entry['sentiment'] for entry in combined_data]
closing_prices = [entry['close'] for entry in combined_data]

# 相関係数を計算
correlation, _ = pearsonr(sentiments, closing_prices)
print(f"Pearson correlation coefficient: {correlation}")

# 散布図の描画
plt.scatter(sentiments, closing_prices)
plt.title('Sentiment vs Stock Closing Price')
plt.xlabel('Sentiment')
plt.ylabel('Stock Closing Price')
plt.show()

print(f"Number of data points: {len(sentiments)}")
print("Sentiments and Closing Prices:")
for sentiment, price in zip(sentiments, closing_prices):
    print(f"Sentiment: {sentiment}, Closing Price: {price}")