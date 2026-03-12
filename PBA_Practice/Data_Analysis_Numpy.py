# ======================== NUMPY DATA ANALYSIS - THEORY ========================
#
# NumPy provides built-in functions for quick data analysis.
# For a numeric array, common measures are:
# 1) Mean (average)
# 2) Sum (total)
# 3) Maximum value
# 4) Minimum value
# 5) Standard deviation (spread of data)
#
# ============================================================================

import numpy as np


# Given array from the question
data = np.array([10, 20, 30, 40, 50])


# 1) Mean
mean_value = np.mean(data)

# 2) Sum
sum_value = np.sum(data)

# 3) Maximum value
max_value = np.max(data)

# 4) Minimum value
min_value = np.min(data)

# 5) Standard deviation
std_deviation = np.std(data)


# ======================== OUTPUT SECTION ========================
if __name__ == "__main__":
	print("Given Data:", data)
	print()

	print("1) Mean:", mean_value)
	print("2) Sum:", sum_value)
	print("3) Maximum value:", max_value)
	print("4) Minimum value:", min_value)
	print("5) Standard deviation:", std_deviation)
