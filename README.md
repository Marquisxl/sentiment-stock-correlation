# News Sentiment and Stock Price Correlation Analysis

## プロジェクトの概要
このプロジェクトは、ニュース記事のセンチメントスコアと特定の企業（例: Apple）の株価終値との間の相関を分析するものです。使用したデータは、NewsAPIから取得したニュース記事と、Alpha Vantage APIから取得した株価データです。

## 使用技術・ツール
- Python
- NewsAPI
- Alpha Vantage API
- TextBlob (センチメント分析)
- SciPy (相関分析)
- Matplotlib (データの可視化)
- dotenv (環境変数管理)

## セットアップ手順

1. **リポジトリをクローン**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2.	仮想環境の作成
　 ```bash
　　python -m venv venv
　　source venv/bin/activate  # Windowsの場合は venv\Scripts\activate

3.	依存パッケージのインストール
　　pip install -r requirements.txt

4.	環境変数の確認
　　.env ファイルは機密情報を含んでいるため、リポジトリには含まれていません。プロジェクトをクローンした後、独　　　　自の .env ファイルを作成し、以下の内容を追加してください:

　　NEWS_API_KEY=your_news_api_key
　　ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key

5.	データの収集と統合
　　python data_integration.py

6.	相関分析とデータの可視化
　　python correlation_analysis.py


プロジェクトの結果

Pearson相関係数は 0.078 であり、これはニュースの感情スコアと株価の終値の間に非常に弱い正の相関があることを示しています。散布図でも、明確な相関が見られないことが確認できます。

今後の改善点

	•	データ量の増加：より長期間のデータを収集して分析する。
	•	モデルの改良：より高度な感情分析モデルを試す。
	•	タイムラグの考慮：ニュースが市場に影響を与えるまでの時間を分析に取り入れる。

