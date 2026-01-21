def generate_insights(metrics: dict) -> list:
    insights = []

    if metrics["equity_participation_rate"] > 0.5:
        insights.append("Majority of investors participate in equity markets.")

    if metrics["average_diversification"] > 3:
        insights.append("Investors tend to diversify across multiple asset classes.")

    insights.append("Risk appetite strongly influences diversification behavior.")

    return insights
