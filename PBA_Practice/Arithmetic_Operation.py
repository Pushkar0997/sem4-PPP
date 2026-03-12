# ======================== NUMPY ARITHMETIC OPERATIONS - THEORY ========================
#
# NumPy supports arithmetic directly on arrays.
#
# Common operations:
# 1) +  -> element-wise addition
# 2) -  -> element-wise subtraction
# 3) *  -> element-wise multiplication
# 4) @  -> matrix multiplication (or np.matmul)
# 5) /  -> element-wise division
#
# Element-wise means operation happens between elements at same position.
# Matrix multiplication follows row x column multiplication rules.
#
# ================================================================================

import numpy as np


# Given arrays from the question
A = np.array([[1, 2],
			  [3, 4]])

B = np.array([[11, 12],
			  [13, 14]])


# 1) Addition of two arrays (element-wise)
addition_result = A + B


# 2) Subtraction of two arrays (element-wise)
subtraction_result = A - B


# 3) Element-wise multiplication
elementwise_multiplication_result = A * B


# 4) Matrix multiplication
# We use @ operator for matrix multiplication.
matrix_multiplication_result = A @ B


# 5) Division of two arrays (element-wise)
division_result = A / B


# ======================== OUTPUT SECTION ========================
if __name__ == "__main__":
	print("Array A:\n", A)
	print("Array B:\n", B)
	print()

	print("1) Addition (A + B):\n", addition_result)
	print()

	print("2) Subtraction (A - B):\n", subtraction_result)
	print()

	print("3) Element-wise Multiplication (A * B):\n", elementwise_multiplication_result)
	print()

	print("4) Matrix Multiplication (A @ B):\n", matrix_multiplication_result)
	print()

	print("5) Division (A / B):\n", division_result)
