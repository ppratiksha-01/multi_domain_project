def generate_insights(metrics: dict, attendance_corr: float) -> list:
    insights = []

    if metrics.get("pass_percentage") is not None:
        insights.append(
            f"Overall pass percentage is {metrics['pass_percentage']:.1f}%."
        )

    if attendance_corr is not None:
        if attendance_corr > 0.5:
            insights.append(
                "Strong positive correlation between attendance and performance."
            )
        else:
            insights.append(
                "Moderate relationship observed between attendance and scores."
            )

    return insights


def generate_recommendations() -> list:
    return [
        "Introduce attendance monitoring and intervention programs.",
        "Provide academic support for low-performing subjects.",
        "Implement early warning systems for at-risk students."
    ]
