# ================= FUNCTIONAL PROGRAMMING COMBINED - THEORY =================
#
# Functional programming tools in Python:
# 1) map()    -> transform each element
# 2) filter() -> keep elements that satisfy condition
# 3) reduce() -> combine elements to one final value
#
# In this file we combine these tools for practical questions.
#
# ===========================================================================

from functools import reduce


# 1) Square all even numbers using filter() and map()
def square_even_numbers(numbers):
	# Step 1: Keep only even numbers
	even_numbers = filter(lambda x: x % 2 == 0, numbers)

	# Step 2: Square each filtered even number
	squared_even_numbers = map(lambda x: x ** 2, even_numbers)

	# Convert map object to list for final output
	return list(squared_even_numbers)


# 2) Find sum of squares of numbers using map() and reduce()
def sum_of_squares(numbers):
	# Step 1: Convert each number to its square
	squared_numbers = map(lambda x: x ** 2, numbers)

	# Step 2: Add all squared values into one result
	total = reduce(lambda a, b: a + b, squared_numbers)
	return total


# 3) Filter even numbers and then calculate their sum using reduce()
def sum_of_even_numbers(numbers):
	# Step 1: Filter even numbers
	even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

	# Handle case where no even numbers are found
	if len(even_numbers) == 0:
		return 0

	# Step 2: Sum filtered even numbers using reduce
	total_even_sum = reduce(lambda a, b: a + b, even_numbers)
	return total_even_sum


# 4) Convert names to uppercase and filter names longer than 5 characters
def uppercase_and_filter_long_names(names):
	# Step 1: Convert all names to uppercase
	uppercase_names = map(str.upper, names)

	# Step 2: Keep only names whose length is greater than 5
	long_names = filter(lambda name: len(name) > 5, uppercase_names)

	# Convert filter object to list for output
	return list(long_names)


# ======================== TEST / OUTPUT SECTION ========================
if __name__ == "__main__":
	nums = [1, 2, 3, 4, 5, 6, 7, 8]

	print("--- 1) Square All Even Numbers ---")
	print("Input:", nums)
	print("Output:", square_even_numbers(nums))
	print()

	print("--- 2) Sum of Squares ---")
	print("Input:", nums)
	print("Output:", sum_of_squares(nums))
	print()

	print("--- 3) Sum of Even Numbers (filter + reduce) ---")
	print("Input:", nums)
	print("Output:", sum_of_even_numbers(nums))
	print()

	print("--- 4) Uppercase Names and Filter Length > 5 ---")
	names_list = ["Aman", "Priyanka", "Rohit", "Anushka", "Dev", "Karanveer"]
	print("Input:", names_list)
	print("Output:", uppercase_and_filter_long_names(names_list))
