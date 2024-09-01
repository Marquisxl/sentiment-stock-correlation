import json
import matplotlib.pyplot as plt
from datetime import datetime

# JSONファイルからデータを読み込む
with open('combined_data.json', 'r') as f:
    combined_data = json.load(f)

# 日付、センチメント、株価のリストを作成
dates = [datetime.strptime(entry['date'], '%Y-%m-%d') for entry in combined_data]
sentiments = [entry['sentiment'] for entry in combined_data]
closing_prices = [entry['close'] for entry in combined_data]

# グラフの描画
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(dates, closing_prices, 'g-')
ax2.plot(dates, sentiments, 'b-')

ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Closing Price', color='g')
ax2.set_ylabel('Sentiment', color='b')

plt.title('News Sentiment and Stock Closing Price Over Time')
plt.show()