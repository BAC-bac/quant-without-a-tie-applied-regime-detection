# Quant Without a Tie: Applied — Regime Detection

A minimal, research-focused implementation of market regime detection using volatility and trend structure.

This repository is part of my ongoing work to bridge trading theory, practical coding, and applied quantitative research.

The goal is simple:
→ Detect when market conditions change  
→ Adapt behaviour accordingly  

Rather than predicting price, this approach focuses on identifying when a strategy is likely to be operating in the wrong environment.

---

## Why This Project Exists

Most trading strategies do not fail because their logic is incorrect.

They fail because they are applied in the wrong market regime.

Regime shifts — changes in volatility, structure, and behaviour — introduce conditions where previously profitable strategies degrade or break entirely.

This project explores a simple, interpretable framework for identifying those shifts.

---

## Key Features

- Simple and interpretable regime classification  
- Uses volatility (ATR-style) and trend structure (EMA)  
- No machine learning — fully transparent logic  
- Designed for integration into trading systems or research pipelines  
- Lightweight and easy to extend  

---

## Project Structure

```text
quant-without-a-tie-applied-regime-detection/
│
├── README.md
├── requirements.txt
│
├── data/
│   └── sample_ohlcv.csv
│
└── src/
    ├── regime_detector.py
    └── example_usage.py
```

---

## How It Works

The regime detector constructs a simple classification pipeline:

1. True Range (volatility proxy)  
2. Rolling ATR estimate  
3. EMA(50) and EMA(200) trend structure  
4. Volatility expansion vs rolling baseline  
5. Rule-based regime classification  

Example regimes include:

- `trend_expansion`  
- `volatile_or_breakdown`  
- `low_volatility`  
- `neutral`  

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/BAC-bac/quant-without-a-tie-applied-regime-detection.git
```

Move into the project folder:

```bash
cd quant-without-a-tie-applied-regime-detection
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run the example:

```bash
python src/example_usage.py
```

---

## Example Usage

```python
import pandas as pd
from src.regime_detector import detect_regime

df = pd.read_csv("data/sample_ohlcv.csv")

regime_df = detect_regime(df)

print(regime_df.tail())
```

---

## Example Output

The script adds additional columns to the original price data, including:

- `atr_14`  
- `atr_50_mean`  
- `ema_50`  
- `ema_200`  
- `trend_up`  
- `volatility_expanding`  
- `regime`  

These columns can then be used for further research, backtesting, or trading system development.

---

## Visual Example (Coming Soon)

Planned visualisation:
- Price series with regime overlays  
- Trend vs volatility expansion phases  
- Identification of unstable market periods  

---

## Philosophy

> Markets are not static. Strategies shouldn't be either.

This project prioritises:

- Simplicity over complexity  
- Robustness over optimisation  
- Adaptation over prediction  
- Clear research logic over overfitted signals  

The purpose is to show how a trading idea can move from concept to code.

---

## Limitations

This implementation is intentionally simple:

- No transaction cost or spread modelling  
- Fixed thresholds (not adaptive)  
- Not validated across multiple instruments  
- Not integrated into a full backtesting framework  

It should be viewed as a research building block, not a production system.

---

## Future Improvements

Possible future additions include:

- Adding spread and execution-cost filters  
- Connecting the detector to a backtest  
- Adding visual regime charts  
- Testing the logic across multiple FX symbols  
- Comparing regime behaviour across different timeframes  

---

## Disclaimer

This project is for educational and research purposes only.

It is not financial advice, investment advice, or a recommendation to trade. Trading and investing involve risk, and past performance does not guarantee future results.
