import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Robust datetime parsing (handles mixed timezones safely)
    if "Formatted Date" in df.columns:
        df["Formatted Date"] = pd.to_datetime(
            df["Formatted Date"],
            utc=True,          # ✅ FIX mixed timezones
            errors="coerce"    # ✅ drop invalid rows safely
        )

        # Drop rows where date parsing failed
        df.dropna(subset=["Formatted Date"], inplace=True)

        # Convert to timezone-naive datetime for analysis
        df["Formatted Date"] = df["Formatted Date"].dt.tz_convert(None)

        # Feature engineering
        df["Year"] = df["Formatted Date"].dt.year
        df["Month"] = df["Formatted Date"].dt.month
        df["Month_Name"] = df["Formatted Date"].dt.month_name()

    return df

