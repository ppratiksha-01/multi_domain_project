def generate_report(metrics, insights) -> str:
    report = f"""
# Finance Investment Analysis Report

## Overview
- Total Investors: {metrics['total_investors']}
- Equity Participation Rate: {metrics['equity_participation_rate']:.2%}
- Average Diversification Score: {metrics['average_diversification']:.2f}

## Key Insights
"""

    for idx, insight in enumerate(insights, 1):
        report += f"{idx}. {insight}\n"

    report += """
## Recommendations
1. Promote diversified portfolios.
2. Offer equity exposure for long-term investors.
3. Design products aligned with risk appetite.
"""

    return report
