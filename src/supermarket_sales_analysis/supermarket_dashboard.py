"""
Supermarket Sales Dashboard
---------------------------
Loads data, prints KPI summary, generates visualizations,
and prints a professional analysis report.

"""

import os
import pandas as pd

from data_loading import load_data
from visualization import (
    plot_daily_sales,
    plot_payment_methods,
    plot_product_sales,
    plot_correlation_heatmap,
    plot_unit_price_hist,
    plot_rating_boxplot
)
from src.supermarket_sales_analysis.analysis import unit_price_distribution


def run_dashboard(csv_path: str, output_dir: str):
    df = load_data(csv_path)

    # ---------------- BASIC INFO ----------------
    print("\n===== SUPERMARKET SALES DASHBOARD =====\n")
    print("Dataset Shape:", df.shape)
    print("\nColumns:", df.columns.tolist())

    total_sales = df["Total"].sum()
    total_transactions = len(df)
    avg_transaction_value = df["Total"].mean()

    # ---------------- REPORT HEADER ----------------
    print("\nSUPERMARKET SALES ANALYSIS REPORT")
    print("=" * 34)

    # ---------------- OVERVIEW ----------------
    df["Date"] = pd.to_datetime(df["Date"])

    period_start = df["Date"].min().strftime("%B %Y")
    period_end = df["Date"].max().strftime("%B %Y")

    print("\n📊 OVERVIEW:")
    print(f"• Total Period: {period_start} - {period_end}")
    print(f"• Total Sales: ₹{total_sales:,.2f}")
    print(f"• Total Transactions: {total_transactions:,}")
    print(f"• Average Transaction Value: ₹{avg_transaction_value:,.2f}")

    # ---------------- TOP PERFORMERS ----------------
    product_sales = (
        df.groupby("Product_Line")["Total"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n🏆 TOP PERFORMERS:")
    for idx, (product, value) in enumerate(product_sales.head(3).items(), start=1):
        percentage = (value / total_sales) * 100
        print(f"{idx}. {product}: ₹{value:,.2f} ({percentage:.1f}%)")

    # ---------------- SALES TRENDS ----------------
    df["Day_Name"] = df["Date"].dt.day_name()
    best_day = (
        df.groupby("Day_Name")["Total"]
        .mean()
        .sort_values(ascending=False)
        .idxmax()
    )

    df["Month"] = df["Date"].dt.month_name()
    best_month = (
        df.groupby("Month")["Total"]
        .sum()
        .sort_values(ascending=False)
        .idxmax()
    )

    df["Hour"] = pd.to_datetime(df["Time"], format="%H:%M").dt.hour
    peak_hours_sales = df.groupby("Hour")["Total"].sum()
    peak_hour = peak_hours_sales.idxmax()
    peak_hour_pct = (peak_hours_sales.max() / peak_hours_sales.sum()) * 100

    print("\n📅 SALES TRENDS:")
    print(f"• Best Day: {best_day}")
    print(f"• Best Month: {best_month}")
    print(f"• Peak Hour: {peak_hour}:00 - {peak_hour + 1}:00 "
          f"({peak_hour_pct:.1f}% of total sales)")

    # ---------------- BUSINESS INSIGHTS ----------------
    print("\n💡 BUSINESS INSIGHTS:")
    print("1. A small number of product lines contribute to the majority of revenue.")
    print("2. Sales peak during specific days and hours, indicating strong time-based buying behavior.")
    print("3. High transaction concentration suggests opportunities for targeted promotions.")

    # ---------------- RECOMMENDATIONS ----------------
    print("\n🎯 RECOMMENDATIONS:")
    print("1. Increase inventory for top-performing product lines.")
    print("2. Launch promotions on high-performing days to maximize revenue.")
    print("3. Optimize staffing and operations during peak sales hours.")

    # ---------------- VISUALIZATION OUTPUT ----------------
    unit_prices = unit_price_distribution(df)
    os.makedirs(output_dir, exist_ok=True)

    plot_daily_sales(df, os.path.join(output_dir, "daily_sales_trend.png"), show=False)
    plot_payment_methods(df, os.path.join(output_dir, "payment_methods.png"), show=False)
    plot_rating_boxplot(df, os.path.join(output_dir, "rating_boxplot.png"), show=False)
    plot_unit_price_hist(unit_prices, os.path.join(output_dir, "unit_price_hist.png"),show=False)
    plot_product_sales(df, os.path.join(output_dir, "product_sales.png"),show=False)
    plot_correlation_heatmap(df, os.path.join(output_dir, "correlation_heatmap.png"),show=False)

    print(f"\n✅ Dashboard visualizations saved to: {output_dir}")


if __name__ == "__main__":
    PROJECT_ROOT = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )

    DATA_PATH = os.path.join(
        PROJECT_ROOT,
        "datasets",
        "supermarket_sales.csv"
    )

    VISUALIZATION_DIR = os.path.join(
        PROJECT_ROOT,
        "visualizations",
        "supermarket"
    )

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at:\n{DATA_PATH}")

    run_dashboard(DATA_PATH, VISUALIZATION_DIR)



