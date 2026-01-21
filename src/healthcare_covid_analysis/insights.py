def generate_insights(metrics: dict):
    insights = []

    if metrics.get("total_confirmed") is not None:
        insights.append(
            f"Total confirmed cases reached {int(metrics['total_confirmed']):,}."
        )

    if metrics.get("total_deaths") is not None:
        insights.append(
            f"Total reported deaths were {int(metrics['total_deaths']):,}."
        )

    insights.append(
        "COVID-19 data shows distinct wave patterns over time."
    )

    return insights


def generate_recommendations():
    return [
        "Strengthen early detection and surveillance systems.",
        "Ensure scalable healthcare infrastructure during peak outbreaks.",
        "Use historical data to guide future pandemic preparedness."
    ]
