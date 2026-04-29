"""
Simple regime detection logic for Quant Without a Tie: Applied.

This module demonstrates how volatility and trend structure can be used
to classify broad market environments.

It is designed as a research example, not a complete trading system.
"""

import pandas as pd


def detect_regime(df: pd.DataFrame) -> pd.DataFrame:
    """
    Detect a simple market regime using:

    - True Range / ATR-style volatility
    - EMA trend structure
    - Volatility expansion compared with recent average ATR

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing at least: open, high, low, close.

    Returns
    -------
    pd.DataFrame
        Original DataFrame with added regime detection columns.
    """

    required_columns = {"open", "high", "low", "close"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    df = df.copy()

    previous_close = df["close"].shift(1)

    df["true_range"] = pd.concat(
        [
            df["high"] - df["low"],
            (df["high"] - previous_close).abs(),
            (df["low"] - previous_close).abs(),
        ],
        axis=1,
    ).max(axis=1)

    df["atr_14"] = df["true_range"].rolling(window=14).mean()
    df["atr_50_mean"] = df["atr_14"].rolling(window=50).mean()

    df["ema_50"] = df["close"].ewm(span=50, adjust=False).mean()
    df["ema_200"] = df["close"].ewm(span=200, adjust=False).mean()

    df["trend_up"] = df["ema_50"] > df["ema_200"]
    df["volatility_expanding"] = df["atr_14"] > df["atr_50_mean"]

    df["regime"] = "neutral"

    df.loc[
        df["trend_up"] & df["volatility_expanding"],
        "regime",
    ] = "trend_expansion"

    df.loc[
        (~df["trend_up"]) & df["volatility_expanding"],
        "regime",
    ] = "volatile_or_breakdown"

    df.loc[
        df["atr_14"] < df["atr_50_mean"],
        "regime",
    ] = "low_volatility"

    return df
