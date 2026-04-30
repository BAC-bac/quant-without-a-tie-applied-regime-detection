import pandas as pd
import matplotlib.pyplot as plt

from regime_detector import detect_regime


def plot_regimes(df: pd.DataFrame) -> None:
    plt.figure(figsize=(14, 7))

    plt.plot(df["close"], label="Price", color="black")

    for regime, color in {
        "trend_expansion": "green",
        "volatile_or_breakdown": "red",
        "low_volatility": "blue",
    }.items():
        mask = df["regime"] == regime
        plt.scatter(
            df.index[mask],
            df["close"][mask],
            label=regime,
            alpha=0.6
        )

    plt.title("Market Regime Detection")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.savefig("regime_visual.png")


def main():
    df = pd.read_csv("data/sample_ohlcv.csv")

    df = detect_regime(df)

    plot_regimes(df)


if __name__ == "__main__":
    main()
