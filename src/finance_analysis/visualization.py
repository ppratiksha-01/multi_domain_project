import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def save_bar(series, title, path: Path, xlabel="", ylabel=""):
    plt.figure(figsize=(8, 4))
    series.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def save_pie(series, title, path: Path):
    plt.figure(figsize=(6, 6))
    series.plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title(title)
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def save_hist(series, title, path: Path):
    plt.figure(figsize=(7, 4))
    plt.hist(series.dropna(), bins=20)
    plt.title(title)
    plt.xlabel(series.name)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def risk_vs_diversification(df, path: Path):
    plt.figure(figsize=(7, 4))
    sns.boxplot(
        data=df.dropna(subset=["Risk_Appetite"]),
        x="Risk_Appetite",
        y="Diversification_Score",
        order=["Low", "Medium", "High"]
    )
    plt.title("Risk Appetite vs Diversification")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def correlation_heatmap(df, path: Path):
    plt.figure(figsize=(7, 5))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Investment Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

