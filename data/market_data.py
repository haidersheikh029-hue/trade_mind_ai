import yfinance as yf


class MarketData:

    @staticmethod
    def get_stock_data(symbol, period="1mo", interval="1d"):
        stock = yf.Ticker(symbol)
        return stock.history(period=period, interval=interval)

    @staticmethod
    def get_latest_price(symbol):
        data = yf.Ticker(symbol).history(period="2d")

        if data.empty:
            return None

        return data["Close"].iloc[-1]