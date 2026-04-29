import pandas as pd


def detect_regime(df: pd.DataFrame) -> pd.DataFrame:
    """
    Detects a simple market regime using:
    - ATR-style volatility
    - EMA trend structure
    - Spread condition

    This is intentionally simple and designed for research clarity.
    """

    df = df.copy()

    df["true_range"] = df[["high", "low", "close"]].apply(
        lambda row: max(
            row["high"] - row["low"],
            abs(row["high"] - row["close"]),
            abs(row["low"] - row["close"])
        ),
        axis=1
    )

    df["atr_14"] = df["true_range"].rolling(14).mean()
    df["atr_50_mean"] = df["atr_14"].rolling(50).mean()

    df["ema_50"] = df["close"].ewm(span=50, adjust=False).mean()
    df["ema_200"] = df["close"].ewm(span=200, adjust=False).mean()

    df["trend_up"] = df["ema_50"] > df["ema_200"]
    df["volatility_expanding"] = df["atr_14"] > df["atr_50_mean"]

    df["regime"] = "neutral"

    df.loc[
        (df["trend_up"]) & (df["volatility_expanding"]),
        "regime"
    ] = "trend_expansion"

    df.loc[
        (~df["trend_up"]) & (df["volatility_expanding"]),
        "regime"
    ] = "volatile_or_breakdown"

    df.loc[
        (df["atr_14"] < df["atr_50_mean"]),
        "regime"
    ] = "low_volatility"

    return df
