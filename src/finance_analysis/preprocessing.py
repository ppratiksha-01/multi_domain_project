import pandas as pd


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess Finance_data.csv:
    - Create Age Groups
    - Create Diversification Score
    - Create Equity Investor flag
    - Create Risk Appetite
    """

    df = df.copy()

    # Age Groups
    df["Age_Group"] = pd.cut(
        df["age"],
        bins=[0, 25, 35, 45, 55, 100],
        labels=["<25", "25-35", "35-45", "45-55", "55+"]
    )

    investment_cols = [
        "Mutual_Funds", "Equity_Market", "Debentures",
        "Government_Bonds", "Fixed_Deposits", "PPF", "Gold"
    ]

    # Diversification Score
    df["Diversification_Score"] = df[investment_cols].sum(axis=1)

    # Equity Participation
    df["Equity_Investor"] = df["Equity_Market"].map({1: "Yes", 0: "No"})

    # Risk Appetite
    df["Factor"] = df["Factor"].astype(str).str.lower()

    def map_risk(factor):
        if "low" in factor:
            return "Low"
        elif "moderate" in factor or "medium" in factor:
            return "Medium"
        elif "high" in factor:
            return "High"
        return None

    df["Risk_Appetite"] = df["Factor"].apply(map_risk)

    return df
