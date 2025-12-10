import yfinance as yf

data = yf.download("AAPL", period="1d", interval="1m")

print(data.tail())
