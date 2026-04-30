"""
Plot detected market regimes.

Run this file from the project root:

python src/plot_regimes.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from regime_detector import detect_regime


def load_sample_data() -> pd.DataFrame:
    """Load the sample OHLCV data used in this repository."""

    df = pd.read_csv("data/sample_ohlcv.csv", sep="\t", header=None)

    df.columns = [
        "time",
        "open",
        "high",
        "low",
        "close",
        "tick_volume",
        "volume",
        "spread",
    ]

    df["time"] = pd.to_datetime(df["time"], dayfirst=True)
    df.set_index("time", inplace=True)

    return df


def plot_regimes(df: pd.DataFrame) -> None:
    """Create and save a price chart with detected regimes overlaid."""

    plt.figure(figsize=(14, 7))

    plt.plot(
        df.index,
        df["close"],
        label="Close Price",
        linewidth=1,
    )

    regimes = {
        "trend_expansion": "Trend Expansion",
        "volatile_or_breakdown": "Volatile / Breakdown",
        "low_volatility": "Low Volatility",
    }

    for regime, label in regimes.items():
        mask = df["regime"] == regime

        plt.scatter(
            df.index[mask],
            df.loc[mask, "close"],
            label=label,
            s=10,
            alpha=0.7,
        )

    plt.title("Quant Without a Tie: Applied — Market Regime Detection")
    plt.xlabel("Time")
    plt.ylabel("Close Price")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    output_dir = Path("images")
    output_dir.mkdir(exist_ok=True)

    plt.savefig(output_dir / "regime_detection_visual.png", dpi=150)
    plt.show()


def main() -> None:
    df = load_sample_data()
    df = detect_regime(df)
    plot_regimes(df)


if __name__ == "__main__":
    main()
