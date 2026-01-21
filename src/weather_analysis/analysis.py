import pandas as pd

def calculate_overview_metrics(df: pd.DataFrame) -> dict:
    metrics = {
        "total_records": len(df),
        "avg_temperature": df["Temperature (C)"].mean() if "Temperature (C)" in df else None,
        "avg_humidity": df["Humidity"].mean() if "Humidity" in df else None,
        "date_range": (
            f"{df['Formatted Date'].min().date()} to {df['Formatted Date'].max().date()}"
            if "Formatted Date" in df else None
        )
    }
    return metrics


def monthly_temperature_average(df: pd.DataFrame) -> pd.Series:
    if "Month_Name" in df and "Temperature (C)" in df:
        return df.groupby("Month_Name")["Temperature (C)"].mean()
    return pd.Series()


def wind_temperature_correlation(df: pd.DataFrame):
    if "Wind Speed (km/h)" in df and "Temperature (C)" in df:
        return df["Wind Speed (km/h)"].corr(df["Temperature (C)"])
    return None
