import pandas as pd


def calculate_overview_metrics(df):
    total_records = len(df)

    confirmed = df["CONFIRMED_COVID"].sum()
    deaths = df["DIED"].sum()
    recovered = confirmed - deaths

    date_range = None
    if df["DIED"].any():
        died_dates = df.loc[df["DIED"], "DATE_DIED_DT"].dropna()
        if not died_dates.empty:
            date_range = (
                f"{died_dates.min().date()} to {died_dates.max().date()}"
            )

    return {
        "total_records": total_records,
        "total_confirmed": confirmed,
        "total_deaths": deaths,
        "total_recovered": recovered,
        "date_range": date_range
    }



def mortality_rate(df):
    confirmed = df["CONFIRMED_COVID"].sum()
    if confirmed == 0:
        return None
    return df["DIED"].sum() / confirmed



def daily_case_trend(df: pd.DataFrame):
    if "Date" in df and "Confirmed" in df:
        return df.groupby("Date")["Confirmed"].sum()
    return pd.Series()


