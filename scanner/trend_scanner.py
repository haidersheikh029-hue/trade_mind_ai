class TrendScanner:

    @staticmethod
    def scan(data):

        latest = data.iloc[-1]

        if (
            latest["EMA_9"] > latest["EMA_20"]
            and latest["EMA_20"] > latest["EMA_50"]
            and latest["RSI"] > 55
            and latest["MACD"] > latest["MACD_SIGNAL"]
        ):
            return "BUY"

        return "NO BUY"