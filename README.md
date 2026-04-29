# Quant Without a Tie: Applied — Regime Detection

This repository accompanies my Medium series, **Quant Without a Tie: Applied**.

The aim is to show how trading concepts such as volatility, trend structure, and regime awareness can be converted into simple, testable Python code.

This is not financial advice and not a complete trading system. It is a research example designed to demonstrate how theory can become a practical framework.

This project is part of my attempt to bridge trading theory, practical coding, and applied quantitative research.
---

## Why This Project Exists

Many trading strategies fail because market conditions change.

A strategy that works well in a clean trend may perform poorly in a noisy or low-volatility environment. This project explores a simple way to classify market regimes using:

- ATR-style volatility
- EMA trend structure
- Volatility expansion versus recent average volatility

The goal is not to predict price direction.  
The goal is to identify when the current environment may or may not suit a particular strategy.

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

The regime detector calculates:

- True Range
- ATR-style volatility
- 50-period EMA
- 200-period EMA
- Volatility expansion
- Simple regime classification

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

## Philosophy

This project prioritises:

- Simplicity over complexity
- Robustness over optimisation
- Adaptation over prediction
- Clear research logic over overfitted signals

The purpose is to show how a trading idea can move from concept to code.

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

