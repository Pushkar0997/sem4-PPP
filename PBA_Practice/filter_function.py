# ======================== PYTHON filter() FUNCTION - THEORY ========================
#
# What is filter()?
# filter() selects items from an iterable based on a condition.
#
# Basic syntax:
# filter(function, iterable)
#
# The function should return:
# - True  -> keep the item
# - False -> discard the item
#
# Important point:
# filter() returns a filter object, so we usually convert it to list.
#
# ================================================================================


# 1) Filter all even numbers from a list using filter()
def filter_even_numbers(numbers):
	# Keep numbers where number % 2 == 0
	return list(filter(lambda x: x % 2 == 0, numbers))


# 2) Filter all odd numbers from a list using filter()
def filter_odd_numbers(numbers):
	# Keep numbers where number % 2 != 0
	return list(filter(lambda x: x % 2 != 0, numbers))


# 3) Filter numbers greater than 50 from a list
def filter_greater_than_50(numbers):
	# Keep numbers strictly greater than 50
	return list(filter(lambda x: x > 50, numbers))


# 4) Filter names that start with letter 'A' from a list
def filter_names_starting_with_a(names):
	# startswith("A") checks if name starts with capital A
	return list(filter(lambda name: name.startswith("A"), names))


# 5) Filter positive numbers from mixed list
def filter_positive_numbers(numbers):
	# Keep numbers greater than 0
	return list(filter(lambda x: x > 0, numbers))


# 6) Filter words with length greater than 5
def filter_words_length_gt_5(words):
	# Keep words where length is more than 5
	return list(filter(lambda word: len(word) > 5, words))


# 7) Filter students whose marks are greater than 60
def filter_students_above_60(student_marks):
	# student_marks is list of tuples: (name, marks)
	# Keep tuple where marks part (index 1) is > 60
	return list(filter(lambda student: student[1] > 60, student_marks))


# ======================== TEST / OUTPUT SECTION ========================
if __name__ == "__main__":
	# Common number list for some examples
	nums = [10, 15, 22, 37, 48, 53, 61, 80]

	print("--- 1) Even Numbers ---")
	print("Input:", nums)
	print("Output:", filter_even_numbers(nums))
	print()

	print("--- 2) Odd Numbers ---")
	print("Input:", nums)
	print("Output:", filter_odd_numbers(nums))
	print()

	print("--- 3) Numbers Greater Than 50 ---")
	print("Input:", nums)
	print("Output:", filter_greater_than_50(nums))
	print()

	print("--- 4) Names Starting With 'A' ---")
	names_list = ["Aman", "Ravi", "Anita", "Priya", "Arjun", "Kiran"]
	print("Input:", names_list)
	print("Output:", filter_names_starting_with_a(names_list))
	print()

	print("--- 5) Positive Numbers ---")
	mixed_numbers = [-10, -3, 0, 5, 12, -7, 20]
	print("Input:", mixed_numbers)
	print("Output:", filter_positive_numbers(mixed_numbers))
	print()

	print("--- 6) Words with Length > 5 ---")
	words_list = ["apple", "banana", "cat", "elephant", "grape", "library"]
	print("Input:", words_list)
	print("Output:", filter_words_length_gt_5(words_list))
	print()

	print("--- 7) Students with Marks > 60 ---")
	students = [
		("Aman", 58),
		("Priya", 76),
		("Rohit", 63),
		("Neha", 49),
		("Kunal", 88),
	]
	print("Input:", students)
	print("Output:", filter_students_above_60(students))
