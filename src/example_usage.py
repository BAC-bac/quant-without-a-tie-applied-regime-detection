import pandas as pd
from regime_detector import detect_regime


df = pd.read_csv("sample_ohlcv.csv")

df = detect_regime(df)

print(df[["close", "atr_14", "ema_50", "ema_200", "regime"]].tail(20))
