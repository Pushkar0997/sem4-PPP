import matplotlib.pyplot as plt


# Sample time-series dataset: Monthly sales
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales_2025 = [120, 135, 128, 150, 165, 160, 175, 180, 170, 190, 200, 210]
sales_2026 = [130, 140, 138, 155, 170, 168, 182, 188, 178, 198, 208, 220]


# Line Plot: Sales trend over time
plt.figure(figsize=(10, 5))
plt.plot(months, sales_2025, marker="o", linewidth=2, label="Sales 2025", color="royalblue")
plt.plot(months, sales_2026, marker="s", linewidth=2, label="Sales 2026", color="darkorange")

plt.title("Monthly Sales Trend Over Time")
plt.xlabel("Month")
plt.ylabel("Sales (in units)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# Expected Output (for report / screenshot section):
# - A line chart with months Jan-Dec on the x-axis and sales on the y-axis.
# - Two lines are shown: Sales 2025 (blue, circle markers) and Sales 2026 (orange, square markers).
# - Both lines show an overall increasing trend with small month-to-month fluctuations.
# - Title, axis labels, legend, and grid are visible for readability.


# FAQs (2-line answers in comments):
# 1. Why use a line plot instead of a bar plot?
# A line plot is better for showing continuous trends and changes over time.
# A bar plot is usually better for comparing separate categories at one point in time.

# 2. How do I add multiple lines to the same plot?
# Call plt.plot() multiple times before plt.show(), each with different y-values.
# Use label=... for each line and then call plt.legend() to identify them.

# 3. How can I save the plot as an image?
# Use plt.savefig("sales_trend.png", dpi=300, bbox_inches="tight") before plt.show().
# This creates a high-quality image file you can insert in your assignment report.

# 4. How do I smooth the line for better visualization?
# You can use interpolation or moving averages to reduce noise in the data.
# Example approach: compute rolling mean using Pandas and plot the smoothed series.

# 5. How do I customize line style and color?
# Use parameters like color=..., linestyle="--", linewidth=..., and marker=... in plt.plot().
# These options help make the chart clearer and visually easier to interpret.
