import pandas as pd

def sales_kpis(df):
    total_sales = df["Total"].sum()
    total_transactions = df.shape[0]
    avg_transaction = df["Total"].mean()
    return total_sales, total_transactions, avg_transaction

def sales_by_product(df):
    return df.groupby("Product_Line")["Total"].sum().sort_values(ascending=False)

def daily_sales(df):
    df["Date"] = pd.to_datetime(df["Date"])
    return df.groupby("Date")["Total"].sum()

def payment_distribution(df):
    return df["Payment"].value_counts()

def rating_analysis(df):
    return df.groupby("Product line")["Rating"].mean().sort_values(ascending=False)

def unit_price_distribution(df):
    """
    Returns unit price column as a Pandas Series (column-safe)
    """
    col_map = {c.lower().replace(" ", "").replace("_", ""): c for c in df.columns}

    unit_price_col = col_map.get("unitprice")

    if not unit_price_col:
        raise KeyError("Unit price column not found in dataset")

    return df[unit_price_col]

