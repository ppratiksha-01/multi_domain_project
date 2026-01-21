import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


def plot_daily_sales(daily_sales, save_path, show=True):
    """
    Expects:
    - daily_sales: Pandas Series
        Index  -> Date
        Values -> Total Sales
    """
    plt.figure(figsize=(10, 5))
    daily_sales.plot()
    plt.title("Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_product_sales(product_sales, save_path, show=True):
    """
    Expects:
    - product_sales: Pandas Series
        Index  -> Product Line
        Values -> Revenue
    """
    plt.figure(figsize=(10, 5))
    product_sales.plot(kind="bar")
    plt.title("Sales by Product Line")
    plt.xlabel("Product Line")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()



def plot_payment_methods(df, save_path,show=True):
    """
    Payment method distribution (Pie Chart)
    Accepts full DataFrame only (P2 standard)
    """
    if "Payment" not in df.columns:
        raise ValueError(
            "plot_payment_methods expects a DataFrame with a 'Payment' column"
        )

    payment_counts = df["Payment"].value_counts()

    plt.figure(figsize=(6, 6))
    payment_counts.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )
    plt.ylabel("")
    plt.title("Payment Method Distribution")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()


def plot_rating_boxplot(df, save_path, show=True):
    """
    Customer rating distribution by product line
    """
    plt.figure(figsize=(8, 5))
    sns.boxplot(
        x="Product_Line",
        y="Rating",
        data=df
    )
    plt.xticks(rotation=45)
    plt.title("Customer Rating Distribution by Product Line")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()

def plot_unit_price_hist(unit_price_series, save_path, show=True):
    """
    unit_price_series: Pandas Series (numeric)
    """
    plt.figure(figsize=(8, 5))
    plt.hist(unit_price_series, bins=20)
    plt.title("Unit Price Distribution")
    plt.xlabel("Unit Price")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()



def plot_correlation_heatmap(df, save_path, show=True):
    """
    Correlation heatmap for numerical features
    """
    numeric_df = df.select_dtypes(include="number")

    plt.figure(figsize=(8, 6))
    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm"
    )
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(save_path)

    if show:
        plt.show()
    else:
        plt.close()

