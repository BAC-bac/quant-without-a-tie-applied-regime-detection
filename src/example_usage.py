"""
Example usage for the simple regime detector.

Run this file from the project root:

python src/example_usage.py
"""

import pandas as pd

from regime_detector import detect_regime


def main() -> None:
    df = pd.read_csv("data/sample_ohlcv.csv")

    regime_df = detect_regime(df)

    columns_to_show = [
        "close",
        "atr_14",
        "atr_50_mean",
        "ema_50",
        "ema_200",
        "trend_up",
        "volatility_expanding",
        "regime",
    ]

    print(regime_df[columns_to_show].tail(20))


if __name__ == "__main__":
    main()
