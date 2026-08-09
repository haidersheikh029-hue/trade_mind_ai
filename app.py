from flask import Flask, render_template

from data.market_data import MarketData
from data.nifty50 import NIFTY50

from indicators.ema import EMAIndicator
from indicators.rsi import RSIIndicator
from indicators.macd import MACDIndicator

from scanner.trend_scanner import TrendScanner

app = Flask(__name__)


@app.route("/")
def home():

    results = []

    for stock in NIFTY50:

        data = MarketData.get_stock_data(
            stock,
            period="6mo",
            interval="1d"
        )

        data = EMAIndicator.add_ema(data)
        data = RSIIndicator.add_rsi(data)
        data = MACDIndicator.add_macd(data)

        signal = TrendScanner.scan(data)

        latest = data.iloc[-1]

        results.append({
            "Stock": stock,
            "Price": round(latest["Close"], 2),
            "RSI": round(latest["RSI"], 2),
            "MACD": round(latest["MACD"], 2),
            "Signal": signal
        })

    return render_template(
        "dashboard.html",
        results=results
    )


if __name__ == "__main__":
    app.run(debug=True)