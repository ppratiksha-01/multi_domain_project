import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Create Pass/Fail based on overall_score
    if "overall_score" in df.columns:
        df["Result"] = df["overall_score"].apply(
            lambda x: "Pass" if x >= 40 else "Fail"
        )

    return df

