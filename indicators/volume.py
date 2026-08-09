import pandas as pd


class VolumeIndicator:

    @staticmethod
    def add_volume_average(data):

        data["Volume_Avg_20"] = (
            data["Volume"]
            .rolling(window=20)
            .mean()
        )

        data["Volume_Ratio"] = (
            data["Volume"] / data["Volume_Avg_20"]
        )

        return data