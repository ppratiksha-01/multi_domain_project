import pandas as pd
from pathlib import Path

from src.finance_analysis.preprocessing import preprocess_data
from src.finance_analysis.analysis import (
    calculate_overview_metrics,
    diversification_by_risk,
    investment_avenue_distribution
)
from src.finance_analysis.visualization import (
    save_bar,
    save_pie,
    risk_vs_diversification,
    correlation_heatmap, save_hist
)
from src.finance_analysis.insights import generate_insights
from src.finance_analysis.report_generator import generate_report


def run_dashboard(data_path: Path, output_dir: Path):
    print("\n===== FINANCE INVESTMENT ANALYSIS DASHBOARD =====\n")

    # -----------------------------
    # Load Data
    # -----------------------------
    df = pd.read_csv(data_path)

    print(f"Dataset Shape: {df.shape}\n")
    print("Columns:", df.columns.tolist(), "\n")

    # -----------------------------
    # Preprocessing
    # -----------------------------
    df = preprocess_data(df)

    # -----------------------------
    # Metrics
    # -----------------------------
    metrics = calculate_overview_metrics(df)

    print("📊 OVERVIEW:")
    print(f"• Total Investors: {metrics['total_investors']}")
    print(f"• Equity Participation Rate: {metrics['equity_participation_rate']:.2%}")
    print(f"• Average Diversification Score: {metrics['average_diversification']:.2f}")

    # -----------------------------
    # Risk Analysis
    # -----------------------------
    risk_div = diversification_by_risk(df)

    print("\n📈 RISK vs DIVERSIFICATION:")
    for risk, score in risk_div.items():
        print(f"• {risk}: {score:.2f}")

    # -----------------------------
    # Insights
    # -----------------------------
    insights = generate_insights(metrics)

    print("\n💡 INSIGHTS:")
    for i, insight in enumerate(insights, 1):
        print(f"{i}. {insight}")

    # -----------------------------
    # Recommendations
    # -----------------------------
    print("\n🎯 RECOMMENDATIONS:")
    print("1. Encourage diversified investment strategies.")
    print("2. Align products with investor risk appetite.")
    print("3. Promote equity exposure for long-term growth.")

    # -------------------------------------------------
    # Visualization Export (NO DISPLAY)
    # -------------------------------------------------
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Investment Avenues
    save_bar(
        df["Investment_Avenues"].value_counts(),
        "Preferred Investment Avenues",
        output_dir / "investment_avenues.png",
        xlabel="Investment Avenue",
        ylabel="Number of Investors"
    )

    # 2. Equity Participation
    save_pie(
        df["Equity_Investor"].value_counts(),
        "Equity Market Participation",
        output_dir / "equity_participation.png"
    )

    # 3. Age Group Distribution
    save_bar(
        df["Age_Group"].value_counts(),
        "Investor Age Group Distribution",
        output_dir / "age_group_distribution.png",
        xlabel="Age Group",
        ylabel="Number of Investors"
    )

    # 4. Risk vs Diversification
    risk_vs_diversification(
        df,
        output_dir / "risk_vs_diversification.png"
    )

    # 5. Diversification Distribution
    save_hist(
        df["Diversification_Score"],
        "Diversification Score Distribution",
        output_dir / "diversification_distribution.png"
    )

    # 6. Correlation Heatmap
    numeric_df = df.select_dtypes(include="number")
    correlation_heatmap(
        numeric_df,
        output_dir / "correlation_heatmap.png"
    )

    # -----------------------------
    # Report Generation (Phase 5 Hook)
    # -----------------------------
    report_text = generate_report(metrics, insights)
    report_path = output_dir / "finance_report.md"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    print("\n📁 Files Exported:")
    print(f"• Visualizations → {output_dir}")
    print(f"• Report → {report_path}")


if __name__ == "__main__":
    PROJECT_ROOT = Path(__file__).resolve().parents[2]

    DATA_PATH = PROJECT_ROOT / "datasets" / "Finance_data.csv"
    VISUALIZATION_DIR = PROJECT_ROOT / "visualizations" / "finance"

    run_dashboard(DATA_PATH, VISUALIZATION_DIR)
