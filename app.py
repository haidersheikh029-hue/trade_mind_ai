from flask import Flask

from data.market_data import MarketData
from indicators.ema import EMAIndicator

app = Flask(__name__)


@app.route("/")
def home():

    data = MarketData.get_stock_data(
        "RELIANCE.NS",
        period="6mo",
        interval="1d"
    )

    data = EMAIndicator.add_ema(data)

    return data.tail(20).to_html()


if __name__ == "__main__":
    app.run(debug=True)