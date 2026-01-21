import pandas as pd

def calculate_overview_metrics(df: pd.DataFrame) -> dict:
    metrics = {
        "total_students": len(df),
        "average_score": df["overall_score"].mean() if "overall_score" in df else None,
        "pass_percentage": (
            (df["Result"] == "Pass").mean() * 100 if "Result" in df else None
        ),
    }
    return metrics


def subject_wise_average(df: pd.DataFrame) -> pd.Series:
    subject_cols = ["math_score", "science_score", "english_score"]
    existing = [c for c in subject_cols if c in df.columns]
    return df[existing].mean()


def attendance_score_correlation(df: pd.DataFrame):
    if "attendance_percentage" in df and "overall_score" in df:
        return df["attendance_percentage"].corr(df["overall_score"])
    return None
