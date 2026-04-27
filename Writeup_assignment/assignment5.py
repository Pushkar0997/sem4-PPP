import matplotlib.pyplot as plt


# Sample dataset
students = ["A", "B", "C", "D", "E"]
marks = [78, 85, 90, 72, 88]
study_hours = [2, 4, 6, 1, 5]


# 1) Bar Plot: Students vs Marks
plt.figure(figsize=(7, 4))
bars = plt.bar(students, marks, color="skyblue", edgecolor="black")
plt.title("Bar Plot: Students vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

# Add labels on top of each bar
for bar in bars:
	h = bar.get_height()
	plt.text(bar.get_x() + bar.get_width() / 2, h + 0.5, f"{int(h)}", ha="center")

plt.ylim(0, 100)
plt.show()


# 2) Scatter Plot: Study Hours vs Marks
plt.figure(figsize=(7, 4))
plt.scatter(study_hours, marks, color="tomato", s=90)
plt.title("Scatter Plot: Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(alpha=0.3)
plt.show()


# Expected Output (for report / screenshot section):
# - First plot: A bar graph with students A-E on x-axis and their marks on y-axis.
# - Bar heights should be: A=78, B=85, C=90, D=72, E=88, with labels on top.
# - Second plot: A scatter graph with study hours on x-axis and marks on y-axis.
# - Points should appear at: (2,78), (4,85), (6,90), (1,72), (5,88).


# FAQs (2-line answers in comments):
# 1. Why use Matplotlib for visualization?
# Matplotlib is simple, flexible, and widely used for creating many kinds of plots.
# It helps represent data visually so trends and relationships are easier to understand.

# 2. How do I change the color of the bars in the bar plot?
# Use the color parameter in plt.bar(), for example color="green" or color=[...].
# You can also set edgecolor, alpha, and other style options for better appearance.

# 3. How do I add data labels on top of bars in the bar plot?
# Loop through the bar objects and use plt.text() at each bar's top position.
# In this code, labels are placed using bar.get_height() and bar.get_x().

# 4. How do I add a trendline to a scatter plot?
# Use NumPy polyfit to compute a best-fit line, then plot it with plt.plot().
# Example: m, b = np.polyfit(x, y, 1) and then plt.plot(x, m*np.array(x)+b).

# 5. Can I save the plots as images?
# Yes, use plt.savefig("filename.png", dpi=300, bbox_inches="tight") before plt.show().
# This saves high-quality image files you can include in reports or assignments.
