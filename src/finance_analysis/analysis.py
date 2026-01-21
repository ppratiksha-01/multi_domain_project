import pandas as pd


def calculate_overview_metrics(df: pd.DataFrame) -> dict:
    return {
        "total_investors": len(df),
        "equity_participation_rate": (
            df["Equity_Investor"].value_counts(normalize=True).get("Yes", 0)
        ),
        "average_diversification": df["Diversification_Score"].mean()
    }


def diversification_by_risk(df: pd.DataFrame) -> pd.Series:
    return (
        df.groupby("Risk_Appetite")["Diversification_Score"]
        .mean()
        .sort_values(ascending=False)
    )


def investment_avenue_distribution(df: pd.DataFrame) -> pd.Series:
    return df["Investment_Avenues"].value_counts()
