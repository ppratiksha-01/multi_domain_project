def generate_report_text(metrics: dict, insights: list, recommendations: list) -> str:
    report = []

    report.append("WEATHER DATA ANALYSIS REPORT\n")
    report.append("OVERVIEW\n")

    for k, v in metrics.items():
        report.append(f"{k.replace('_', ' ').title()}: {v}")

    report.append("\nINSIGHTS")
    for i in insights:
        report.append(f"- {i}")

    report.append("\nRECOMMENDATIONS")
    for r in recommendations:
        report.append(f"- {r}")

    return "\n".join(report)
