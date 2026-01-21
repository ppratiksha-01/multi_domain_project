import os
import pandas as pd
from pathlib import Path

from src.weather_analysis.preprocessing import preprocess_data
from src.weather_analysis.analysis import (
    calculate_overview_metrics,
    monthly_temperature_average,
    wind_temperature_correlation
)
from src.weather_analysis.insights import (
    generate_insights,
    generate_recommendations
)
from src.weather_analysis.visualization import (
    plot_monthly_temperature,
    plot_weather_summary,
    plot_wind_vs_temperature
)

from src.weather_analysis.visualization import (
    plot_temperature_trend,
    plot_humidity_distribution,
    plot_pressure_vs_temperature,
    plot_correlation_heatmap
)



def run_dashboard(data_path: Path, output_dir: Path):
    # -------------------------------------------------
    # Load & preprocess data
    # -------------------------------------------------
    df = pd.read_csv(data_path)
    df = preprocess_data(df)

    print("\n===== WEATHER ANALYSIS DASHBOARD =====\n")
    print(f"Dataset Shape: {df.shape}\n")
    print(f"Columns: {list(df.columns)}\n")

    # -------------------------------------------------
    # KPIs & Metrics
    # -------------------------------------------------
    metrics = calculate_overview_metrics(df)
    wind_temp_corr = wind_temperature_correlation(df)

    print("WEATHER DATA ANALYSIS REPORT")
    print("=" * 38)

    print("\n📊 OVERVIEW:")
    print(f"• Total Records: {metrics['total_records']}")

    if metrics.get("date_range"):
        print(f"• Date Range: {metrics['date_range']}")
    else:
        print("• Date Range: Not Available")

    if metrics.get("avg_temperature") is not None:
        print(f"• Average Temperature: {metrics['avg_temperature']:.2f} °C")
    else:
        print("• Average Temperature: Not Available")

    if metrics.get("avg_humidity") is not None:
        print(f"• Average Humidity: {metrics['avg_humidity']:.2f}")
    else:
        print("• Average Humidity: Not Available")

    # -------------------------------------------------
    # Temperature Trends
    # -------------------------------------------------
    print("\n🌡️ TEMPERATURE TRENDS:")
    monthly_avg = monthly_temperature_average(df)

    if not monthly_avg.empty:
        hottest_month = monthly_avg.idxmax()
        coldest_month = monthly_avg.idxmin()
        print(f"• Hottest Month (Avg): {hottest_month}")
        print(f"• Coldest Month (Avg): {coldest_month}")
    else:
        print("• Monthly temperature data not available")

    # -------------------------------------------------
    # Weather Correlation
    # -------------------------------------------------
    print("\n💨 WEATHER CORRELATION:")
    if wind_temp_corr is not None:
        print(f"• Wind–Temperature Correlation: {wind_temp_corr:.2f}")
    else:
        print("• Wind–Temperature Correlation: Not Available")

    # -------------------------------------------------
    # Insights & Recommendations
    # -------------------------------------------------
    insights = generate_insights(metrics, wind_temp_corr)
    recommendations = generate_recommendations()

    print("\n💡 INSIGHTS:")
    for i, insight in enumerate(insights, start=1):
        print(f"{i}. {insight}")

    print("\n🎯 RECOMMENDATIONS:")
    for i, rec in enumerate(recommendations, start=1):
        print(f"{i}. {rec}")

    # -------------------------------------------------
    # Visualization Export (NO DISPLAY)
    # -------------------------------------------------
    os.makedirs(output_dir, exist_ok=True)

    if not monthly_avg.empty:
        plot_monthly_temperature(
            monthly_avg,
            output_dir / "monthly_temperature.png",
            show=False
        )

    if "Summary" in df.columns:
        plot_weather_summary(
            df["Summary"].value_counts().head(10),
            output_dir / "weather_summary_frequency.png",
            show=False
        )

    if "Wind Speed (km/h)" in df.columns and "Temperature (C)" in df.columns:
        plot_wind_vs_temperature(
            df["Wind Speed (km/h)"],
            df["Temperature (C)"],
            output_dir / "wind_vs_temperature.png",
            show=False
        )

    # -------------------------------------------------
    # Additional Visualizations
    # -------------------------------------------------

    if "Formatted Date" in df.columns and "Temperature (C)" in df.columns:
        plot_temperature_trend(
            df["Formatted Date"],
            df["Temperature (C)"],
            output_dir / "temperature_trend.png",
            show=False
        )

    if "Humidity" in df.columns:
        plot_humidity_distribution(
            df["Humidity"],
            output_dir / "humidity_distribution.png",
            show=False
        )

    if "Pressure (millibars)" in df.columns and "Temperature (C)" in df.columns:
        plot_pressure_vs_temperature(
            df["Pressure (millibars)"],
            df["Temperature (C)"],
            output_dir / "pressure_vs_temperature.png",
            show=False
        )

    numeric_df = df.select_dtypes(include="number")
    plot_correlation_heatmap(
        numeric_df,
        output_dir / "correlation_heatmap.png",
        show=False
    )


if __name__ == "__main__":
    PROJECT_ROOT = Path(__file__).resolve().parents[2]

    DATA_PATH = PROJECT_ROOT / "datasets" / "weatherHistory.csv"
    VISUALIZATION_DIR = PROJECT_ROOT / "visualizations" / "weather"

    run_dashboard(DATA_PATH, VISUALIZATION_DIR)
