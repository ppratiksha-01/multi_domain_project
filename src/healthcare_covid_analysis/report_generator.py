def generate_report_text(metrics: dict, insights: list, recommendations: list) -> str:
    report = []

    report.append("COVID-19 DATA ANALYSIS REPORT\n")
    report.append("OVERVIEW")

    for key, value in metrics.items():
        report.append(f"{key.replace('_', ' ').title()}: {value}")

    report.append("\nINSIGHTS")
    for i in insights:
        report.append(f"- {i}")

    report.append("\nRECOMMENDATIONS")
    for r in recommendations:
        report.append(f"- {r}")

    return "\n".join(report)
