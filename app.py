from flask import Flask, render_template

from data.market_data import MarketData
from data.nifty50 import NIFTY50

from indicators.ema import EMAIndicator
from indicators.rsi import RSIIndicator
from indicators.macd import MACDIndicator
from indicators.volume import VolumeIndicator

from scanner.trend_scanner import TrendScanner
from scanner.confidence import ConfidenceScore

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
        data = VolumeIndicator.add_volume_average(data)

        signal = TrendScanner.scan(data)
        score = ConfidenceScore.calculate(data)
        if score >= 80:
            strength = "STRONG BUY"
        elif score >= 60:
            strength = "BUY"
        elif score >= 40:
            strength = "WATCH"
        else:
            strength = "NO BUY"
        latest = data.iloc[-1]
        if latest["EMA_9"] > latest["EMA_20"] > latest["EMA_50"]:
            trend = "Bullish"
        else:
            trend = "Bearish"
    

        results.append({
            "Stock": stock,
            "Price": round(latest["Close"], 2),
            "RSI": round(latest["RSI"], 2),
            "Trend": trend,
            "MACD": round(latest["MACD"], 2),
            "Volume_Ratio": round(latest["Volume_Ratio"], 2),
            "Score": score,
            "Strength": strength,
            "Signal": signal,
            
        })
    results = sorted(
        results,
        key=lambda x: x["Score"],
        reverse=True
    )

    return render_template(
        "dashboard.html",
        results=results
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)