# ======================== PYTHON map() FUNCTION - THEORY ========================
#
# What is map()?
# map() applies a function to each item of an iterable (like list) and returns
# a map object (iterator).
#
# Basic syntax:
# map(function, iterable)
# map(function, iterable1, iterable2, ...)
#
# Important point:
# map() returns a map object, so we usually convert result to list using list().
#
# ===============================================================================


# 1) Double all numbers in a list using map()
def double_numbers(numbers):
	# lambda x: x * 2 means each number is multiplied by 2
	doubled = list(map(lambda x: x * 2, numbers))
	return doubled


# 2) Convert Celsius temperatures to Fahrenheit using map()
def celsius_to_fahrenheit_list(celsius_list):
	# Formula: F = (C * 9/5) + 32
	fahrenheit_list = list(map(lambda c: (c * 9 / 5) + 32, celsius_list))
	return fahrenheit_list


# 3) Find square of each number using map()
def square_numbers(numbers):
	# Each number is raised to power 2
	squared = list(map(lambda x: x ** 2, numbers))
	return squared


# 4) Convert list of strings to uppercase using map()
def convert_to_uppercase(words):
	# str.upper converts each string to uppercase
	upper_words = list(map(str.upper, words))
	return upper_words


# 5) Add two lists element-wise using map()
def add_two_lists(list1, list2):
	# lambda x, y: x + y adds corresponding elements from both lists
	added = list(map(lambda x, y: x + y, list1, list2))
	return added


# 6) Calculate cube of numbers using map() and lambda
def cube_numbers(numbers):
	# Each number is raised to power 3
	cubed = list(map(lambda x: x ** 3, numbers))
	return cubed


# 7) Calculate length of each word in a list using map()
def word_lengths(words):
	# len function returns length of each word
	lengths = list(map(len, words))
	return lengths


# ======================== TEST / OUTPUT SECTION ========================
if __name__ == "__main__":
	# Example list for numeric operations
	nums = [1, 2, 3, 4, 5]

	print("--- 1) Double all numbers ---")
	print("Input:", nums)
	print("Output:", double_numbers(nums))
	print()

	print("--- 2) Celsius to Fahrenheit ---")
	celsius_values = [0, 25, 37, 100]
	print("Input:", celsius_values)
	print("Output:", celsius_to_fahrenheit_list(celsius_values))
	print()

	print("--- 3) Square of each number ---")
	print("Input:", nums)
	print("Output:", square_numbers(nums))
	print()

	print("--- 4) Convert strings to uppercase ---")
	words_list = ["python", "map", "function", "practice"]
	print("Input:", words_list)
	print("Output:", convert_to_uppercase(words_list))
	print()

	print("--- 5) Add two lists element-wise ---")
	list_a = [10, 20, 30]
	list_b = [1, 2, 3]
	print("List A:", list_a)
	print("List B:", list_b)
	print("Output:", add_two_lists(list_a, list_b))
	print()

	print("--- 6) Cube of numbers using map() and lambda ---")
	print("Input:", nums)
	print("Output:", cube_numbers(nums))
	print()

	print("--- 7) Length of each word ---")
	words_for_length = ["apple", "banana", "kiwi", "watermelon"]
	print("Input:", words_for_length)
	print("Output:", word_lengths(words_for_length))
