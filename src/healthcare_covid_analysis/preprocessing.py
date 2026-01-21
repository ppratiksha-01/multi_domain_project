import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Ensure DATE_DIED is string
    df["DATE_DIED"] = df["DATE_DIED"].astype(str)

    # COVID confirmed (1,2,3 = positive)
    df["CONFIRMED_COVID"] = df["CLASIFFICATION_FINAL"].isin([1, 2, 3])

    # Death flag
    df["DIED"] = df["DATE_DIED"] != "9999-99-99"

    # Create a CLEAN datetime column for deaths only
    df["DATE_DIED_DT"] = pd.NaT
    df.loc[df["DIED"], "DATE_DIED_DT"] = pd.to_datetime(
        df.loc[df["DIED"], "DATE_DIED"],
        errors="coerce"
    )

    return df

