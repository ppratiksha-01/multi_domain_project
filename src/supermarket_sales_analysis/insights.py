def generate_insights(total_sales, avg_transaction, top_product):
    insights = [
        f"Total revenue generated is ₹{total_sales:,.2f}",
        f"Average transaction value is ₹{avg_transaction:,.2f}",
        f"Top performing product line is {top_product}"
    ]
    return insights
