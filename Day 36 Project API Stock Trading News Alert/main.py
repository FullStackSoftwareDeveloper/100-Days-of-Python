import requests

# Fictional data used for demonstration purposes

news_parameters = {
    "q": "tesla",
    "from": "2024-04-01",
    "sortBy": "publishedAt",
    "apiKey": "your_api_key",
}

# All articles about Tesla from April, sorted by recent first
news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
news_data = news_response.json()
print(news_data)

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": "your_api_key",
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
data = response.json()
today = data["Time Series (Daily)"]["2024-04-02"]["4. close"]
yesterday = data["Time Series (Daily)"]["2024-04-01"]["4. close"]

trend = float(today) - float(yesterday)

if trend < 0:
    print(str(round(trend, 2)) + " per share, downwards trend")
else:
    print(str(round(trend, 2)) + " per share, upwards trend")