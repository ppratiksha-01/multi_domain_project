def generate_insights(metrics: dict, wind_temp_corr):
    insights = []

    if metrics.get("avg_temperature") is not None:
        insights.append(
            f"Average recorded temperature is {metrics['avg_temperature']:.2f}°C."
        )

    if wind_temp_corr is not None:
        if abs(wind_temp_corr) > 0.5:
            insights.append(
                "Strong relationship observed between wind speed and temperature."
            )
        else:
            insights.append(
                "Wind speed shows weak to moderate correlation with temperature."
            )

    return insights


def generate_recommendations():
    return [
        "Incorporate seasonal trends into weather forecasting models.",
        "Monitor wind and temperature interactions for climate studies.",
        "Use historical data to plan for extreme weather conditions."
    ]
