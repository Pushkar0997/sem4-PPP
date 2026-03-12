# ======================== NUMPY BASICS - THEORY ========================
#
# What is NumPy?
# NumPy is a Python library used for numerical operations.
# Main object in NumPy is ndarray (array object).
#
# Why use NumPy arrays instead of Python lists?
# 1. Faster for numerical computation.
# 2. Supports multi-dimensional arrays easily.
# 3. Provides many built-in functions (arange, zeros, ones, reshape, etc.).
#
# In this file, each function solves one beginner program-based question.
# ======================================================================

import numpy as np


# 1) Create array with elements [10, 20, 30, 40, 50]
def create_simple_array():
	# np.array() creates a NumPy array from Python list.
	arr = np.array([10, 20, 30, 40, 50])
	return arr


# 2) Create 2D array from given data
def create_2d_array():
	# 2D array means rows and columns (matrix form).
	arr_2d = np.array([
		[10, 20, 30],
		[40, 50, 60],
		[70, 80, 90]
	])
	return arr_2d


# 3) Create array using np.arange(1, 8)
def create_arange_array():
	# np.arange(start, stop) includes start and excludes stop.
	# So np.arange(1, 8) gives: 1,2,3,4,5,6,7
	arr = np.arange(1, 8)
	return arr


# 4) Create array of five zeros
def create_zeros_array():
	# np.zeros(5) creates 1D array with five 0.0 values.
	arr = np.zeros(5)
	return arr


# 5) Create 2x3 array of ones
def create_ones_matrix():
	# np.ones((rows, cols)) creates matrix filled with 1.0.
	arr = np.ones((2, 3))
	return arr


# 6) Reshape 1D array to 2x3 matrix
def reshape_array_to_2x3():
	# Start with a 1D array of 6 elements.
	one_d = np.array([1, 2, 3, 4, 5, 6])

	# reshape(2, 3) converts 1D array into 2 rows and 3 columns.
	two_d = one_d.reshape(2, 3)
	return one_d, two_d


# ======================== TEST / OUTPUT SECTION ========================
if __name__ == "__main__":
	print("--- 1) Array [10, 20, 30, 40, 50] ---")
	print(create_simple_array())
	print()

	print("--- 2) Given 2D Array ---")
	print(create_2d_array())
	print()

	print("--- 3) Array using np.arange(1, 8) ---")
	print(create_arange_array())
	print()

	print("--- 4) Array of Five Zeros ---")
	print(create_zeros_array())
	print()

	print("--- 5) 2x3 Array of Ones ---")
	print(create_ones_matrix())
	print()

	print("--- 6) Reshape 1D Array to 2x3 ---")
	original, reshaped = reshape_array_to_2x3()
	print("Original 1D:", original)
	print("Reshaped 2x3:\n", reshaped)
