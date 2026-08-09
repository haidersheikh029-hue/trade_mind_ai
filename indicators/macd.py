import pandas as pd


class MACDIndicator:

    @staticmethod
    def add_macd(data):

        ema12 = data["Close"].ewm(span=12, adjust=False).mean()
        ema26 = data["Close"].ewm(span=26, adjust=False).mean()

        data["MACD"] = ema12 - ema26
        data["MACD_SIGNAL"] = (
            data["MACD"]
            .ewm(span=9, adjust=False)
            .mean()
        )

        data["MACD_HIST"] = (
            data["MACD"]
            - data["MACD_SIGNAL"]
        )

        return data