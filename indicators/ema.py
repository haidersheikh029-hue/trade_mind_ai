import pandas_ta as ta


class EMAIndicator:

    @staticmethod
    def add_ema(data):
        """
        Add EMA 9, EMA 20 and EMA 50 columns
        """

        data["EMA_9"] = ta.ema(data["Close"], length=9)
        data["EMA_20"] = ta.ema(data["Close"], length=20)
        data["EMA_50"] = ta.ema(data["Close"], length=50)

        return data