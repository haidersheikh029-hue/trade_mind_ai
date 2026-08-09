class ConfidenceScore:

    @staticmethod
    def calculate(data):

        latest = data.iloc[-1]

        score = 0

        # EMA Trend = 30 points
        if latest["EMA_9"] > latest["EMA_20"] > latest["EMA_50"]:
            score += 30

        # RSI = 20 points
        if latest["RSI"] > 55:
            score += 20

        # MACD = 20 points
        if latest["MACD"] > latest["MACD_SIGNAL"]:
            score += 20

        # Price above EMA20 = 20 points
        if latest["Close"] > latest["EMA_20"]:
            score += 20

        # Volume Confirmation = 10 points
        if latest["Volume_Ratio"] >= 1.0:
            score += 10

        return score