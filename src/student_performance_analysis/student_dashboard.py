import os
import pandas as pd
from pathlib import Path


from src.student_performance_analysis.preprocessing import preprocess_data
from src.student_performance_analysis.analysis import (
    calculate_overview_metrics,
    subject_wise_average,
    attendance_score_correlation
)
from src.student_performance_analysis.insights import (
    generate_insights,
    generate_recommendations
)
from src.student_performance_analysis.visualization import (
    plot_subject_averages,
    plot_pass_fail,
    plot_attendance_vs_score
)

from src.student_performance_analysis.visualization import (
    plot_score_distribution,
    plot_gender_vs_score,
    plot_study_hours_vs_score,
    plot_correlation_heatmap
)




def run_dashboard(data_path: str, output_dir: str):
    # -------------------------------------------------
    # Load & preprocess data
    # -------------------------------------------------
    df = pd.read_csv(data_path)
    df = preprocess_data(df)

    print("\n===== STUDENT PERFORMANCE DASHBOARD =====\n")
    print(f"Dataset Shape: {df.shape}\n")
    print(f"Columns: {list(df.columns)}\n")

    # -------------------------------------------------
    # KPIs & Metrics
    # -------------------------------------------------
    metrics = calculate_overview_metrics(df)
    attendance_corr = attendance_score_correlation(df)

    print("STUDENT PERFORMANCE ANALYSIS REPORT")
    print("=" * 38)

    print("\n📊 OVERVIEW:")
    print(f"• Total Students: {metrics['total_students']}")
    avg_score = metrics.get("average_score")
    pass_pct = metrics.get("pass_percentage")

    print(f"• Total Students: {metrics['total_students']}")

    if avg_score is not None:
        print(f"• Average Score: {avg_score:.2f}")
    else:
        print("• Average Score: Not Available")

    if pass_pct is not None:
        print(f"• Pass Percentage: {pass_pct:.2f}%")
    else:
        print("• Pass Percentage: Not Available")

    # -------------------------------------------------
    # Subject Performance
    # -------------------------------------------------
    subject_avg = subject_wise_average(df)

    print("\n📚 SUBJECT PERFORMANCE:")
    for subject, avg in subject_avg.items():
        print(f"• {subject}: {avg:.2f}")

    # -------------------------------------------------
    # Attendance Impact
    # -------------------------------------------------
    print("\n📈 ATTENDANCE IMPACT:")
    if attendance_corr is not None:
        print(f"• Attendance–Score Correlation: {attendance_corr:.2f}")
    else:
        print("• Attendance–Score Correlation: Not Available")

    # -------------------------------------------------
    # Insights & Recommendations
    # -------------------------------------------------
    insights = generate_insights(metrics, attendance_corr)
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

    if "Result" in df.columns:
        plot_pass_fail(
            df["Result"].value_counts(),
            os.path.join(output_dir, "pass_fail.png"),
            show=False
        )

    plot_subject_averages(
        subject_avg,
        os.path.join(output_dir, "subject_avg_scores.png"),
        show=False
    )

    if "attendance_percentage" in df.columns and "overall_score" in df.columns:
        plot_attendance_vs_score(
            df["attendance_percentage"],
            df["overall_score"],
            os.path.join(output_dir, "attendance_vs_score.png"),
            show=False
        )

    # Additional visualizations
    plot_score_distribution(
        df["overall_score"],
        os.path.join(output_dir, "score_distribution.png"),
        show=False
    )

    if "gender" in df.columns:
        plot_gender_vs_score(
            df["gender"],
            df["overall_score"],
            os.path.join(output_dir, "gender_vs_score.png"),
            show=False
        )

    if "study_hours" in df.columns:
        plot_study_hours_vs_score(
            df["study_hours"],
            df["overall_score"],
            os.path.join(output_dir, "study_hours_vs_score.png"),
            show=False
        )

    numeric_df = df.select_dtypes(include="number")
    plot_correlation_heatmap(
        numeric_df,
        os.path.join(output_dir, "correlation_heatmap.png"),
        show=False
    )


if __name__ == "__main__":
    PROJECT_ROOT = Path(__file__).resolve().parents[2]

    DATA_PATH = PROJECT_ROOT / "datasets" / "Student_Performance.csv"
    VISUALIZATION_DIR = PROJECT_ROOT / "visualizations" / "student"

    run_dashboard(DATA_PATH, VISUALIZATION_DIR)

