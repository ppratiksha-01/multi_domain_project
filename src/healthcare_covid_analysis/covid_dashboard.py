import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from src.healthcare_covid_analysis.preprocessing import preprocess_data
from src.healthcare_covid_analysis.analysis import (
    calculate_overview_metrics,
    mortality_rate
)
from src.healthcare_covid_analysis.insights import (
    generate_insights,
    generate_recommendations
)
from src.healthcare_covid_analysis.visualization import (
    plot_correlation_heatmap
)


def run_dashboard(data_path: Path, output_dir: Path):
    # -------------------------------------------------
    # Load & preprocess data
    # -------------------------------------------------
    df = pd.read_csv(data_path)
    df = preprocess_data(df)

    print("\n===== COVID-19 ANALYSIS DASHBOARD =====\n")
    print(f"Dataset Shape: {df.shape}\n")
    print("Columns:", df.columns.tolist(), "\n")

    # -------------------------------------------------
    # OVERVIEW METRICS
    # -------------------------------------------------
    metrics = calculate_overview_metrics(df)
    mortality = mortality_rate(df)

    print("COVID-19 DATA ANALYSIS REPORT")
    print("=" * 42)

    print("\n📊 OVERVIEW:")
    print(f"• Total Records: {metrics['total_records']}")
    print(f"• Date Range: {metrics['date_range']}")
    print(f"• Total Confirmed Cases: {metrics['total_confirmed']:,}")
    print(f"• Total Deaths: {metrics['total_deaths']:,}")
    print(f"• Total Recovered: {metrics['total_recovered']:,}")

    print("\n📈 CASE SUMMARY:")
    print(f"• Confirmed COVID Patients: {metrics['total_confirmed']:,}")
    print(f"• Deaths: {metrics['total_deaths']:,}")
    print(f"• Recoveries (Alive): {metrics['total_recovered']:,}")

    print("\n⚠️ MORTALITY ANALYSIS:")
    if mortality is not None:
        print(f"• Average Mortality Rate: {mortality:.4f}")
    else:
        print("• Mortality data not available")

    # -------------------------------------------------
    # INSIGHTS & RECOMMENDATIONS
    # -------------------------------------------------
    print("\n💡 INSIGHTS:")
    for i, insight in enumerate(generate_insights(metrics), start=1):
        print(f"{i}. {insight}")

    print("\n🎯 RECOMMENDATIONS:")
    for i, rec in enumerate(generate_recommendations(), start=1):
        print(f"{i}. {rec}")

    # -------------------------------------------------
    # VISUALIZATION EXPORT (CLINICAL DATASET)
    # -------------------------------------------------
    os.makedirs(output_dir, exist_ok=True)

    # 1. Deaths over time
    death_dates = df.loc[df["DIED"], "DATE_DIED_DT"].dropna()
    deaths_by_date = death_dates.value_counts().sort_index()

    if not deaths_by_date.empty:
        plt.figure(figsize=(10, 4))
        deaths_by_date.plot()
        plt.title("COVID-19 Deaths Over Time")
        plt.xlabel("Date")
        plt.ylabel("Number of Deaths")
        plt.tight_layout()
        plt.savefig(output_dir / "deaths_over_time.png")
        plt.close()

    # 2. Active cases trend (clinical proxy)
    total_confirmed = df["CONFIRMED_COVID"].sum()
    cumulative_deaths = deaths_by_date.cumsum()
    active_cases = total_confirmed - cumulative_deaths

    plt.figure(figsize=(10, 4))
    plt.plot(active_cases.index, active_cases.values)
    plt.title("Active COVID-19 Cases Trend (Clinical Proxy)")
    plt.xlabel("Date")
    plt.ylabel("Active Cases")
    plt.tight_layout()
    plt.savefig(output_dir / "active_cases_trend.png")
    plt.close()

    # 3. Mortality rate trend (IMPORTANT: no name collision)
    mortality_rate_trend = cumulative_deaths / total_confirmed

    plt.figure(figsize=(10, 4))
    plt.plot(mortality_rate_trend.index, mortality_rate_trend.values)
    plt.title("COVID-19 Mortality Rate Trend")
    plt.xlabel("Date")
    plt.ylabel("Mortality Rate")
    plt.tight_layout()
    plt.savefig(output_dir / "mortality_rate_trend.png")
    plt.close()

    # 4. Confirmed vs Deaths
    counts = {
        "Confirmed": total_confirmed,
        "Deaths": df["DIED"].sum()
    }

    plt.figure(figsize=(6, 4))
    plt.bar(counts.keys(), counts.values())
    plt.title("Confirmed vs Deaths")
    plt.ylabel("Number of Patients")
    plt.tight_layout()
    plt.savefig(output_dir / "confirmed_vs_deaths.png")
    plt.close()

    # 5. Top Medical Units by confirmed cases
    top_units = (
        df[df["CONFIRMED_COVID"]]
        .groupby("MEDICAL_UNIT")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(8, 4))
    top_units.plot(kind="bar")
    plt.title("Top 10 Medical Units by Confirmed COVID Cases")
    plt.xlabel("Medical Unit")
    plt.ylabel("Confirmed Patients")
    plt.tight_layout()
    plt.savefig(output_dir / "top_medical_units.png")
    plt.close()

    # 6. Correlation heatmap
    numeric_df = df.select_dtypes(include="number")
    if not numeric_df.empty:
        plot_correlation_heatmap(
            numeric_df,
            output_dir / "correlation_heatmap.png",
            show=False
        )

    print("\n✅ Visualization export completed.")
    print("Generated files:")
    for f in output_dir.iterdir():
        print(" -", f.name)


if __name__ == "__main__":
    PROJECT_ROOT = Path(__file__).resolve().parents[2]

    DATA_PATH = PROJECT_ROOT / "datasets" / "Covid Data.csv"
    VISUALIZATION_DIR = PROJECT_ROOT / "visualizations" / "healthcare"

    run_dashboard(DATA_PATH, VISUALIZATION_DIR)
