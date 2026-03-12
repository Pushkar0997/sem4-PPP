# ======================== PYTHON reduce() FUNCTION - THEORY ========================
#
# What is reduce()?
# reduce() repeatedly applies a function to items of an iterable and reduces
# them to one final value.
#
# It is available in functools module.
#
# Basic syntax:
# from functools import reduce
# reduce(function, iterable)
#
# Example idea:
# [1, 2, 3, 4] -> (((1 op 2) op 3) op 4)
#
# ================================================================================

from functools import reduce


# 1) Find sum of all elements in a list using reduce()
def sum_of_list(numbers):
	# Add elements one by one
	return reduce(lambda a, b: a + b, numbers)


# 2) Find product of elements in a list using reduce()
def product_of_list(numbers):
	# Multiply elements one by one
	return reduce(lambda a, b: a * b, numbers)


# 3) Find maximum element in a list using reduce()
def max_in_list(numbers):
	# Keep bigger value between a and b at each step
	return reduce(lambda a, b: a if a > b else b, numbers)


# 4) Calculate factorial of a number using reduce()
def factorial_using_reduce(n):
	# Factorial of n = 1 * 2 * 3 * ... * n
	# range(1, n+1) gives numbers from 1 to n
	if n < 0:
		return "Factorial not defined for negative numbers"
	if n == 0 or n == 1:
		return 1
	return reduce(lambda a, b: a * b, range(1, n + 1))


# 5) Multiply all elements of a list using reduce() and lambda
def multiply_all_elements(numbers):
	# Same multiplication logic as product, shown separately as asked
	return reduce(lambda a, b: a * b, numbers)


# ======================== TEST / OUTPUT SECTION ========================
if __name__ == "__main__":
	nums = [2, 4, 6, 8]

	print("--- 1) Sum of List Elements ---")
	print("Input:", nums)
	print("Output:", sum_of_list(nums))
	print()

	print("--- 2) Product of List Elements ---")
	print("Input:", nums)
	print("Output:", product_of_list(nums))
	print()

	print("--- 3) Maximum Element in List ---")
	nums_for_max = [15, 42, 7, 99, 31]
	print("Input:", nums_for_max)
	print("Output:", max_in_list(nums_for_max))
	print()

	print("--- 4) Factorial Using reduce() ---")
	n = 5
	print("Input:", n)
	print("Output:", factorial_using_reduce(n))
	print()

	print("--- 5) Multiply All Elements Using reduce() and lambda ---")
	nums_for_multiply = [3, 5, 2, 4]
	print("Input:", nums_for_multiply)
	print("Output:", multiply_all_elements(nums_for_multiply))
