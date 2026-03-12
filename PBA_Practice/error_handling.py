# ======================== PYTHON ERROR HANDLING - THEORY ========================
#
# Why error handling?
# Programs can crash if unexpected input/error occurs.
# try-except lets us handle errors gracefully.
#
# Main blocks:
# 1) try     -> code that may cause error
# 2) except  -> runs if matching error occurs
# 3) else    -> runs if no error in try block
# 4) finally -> always runs (error happens or not)
#
# Common exceptions used here:
# - ZeroDivisionError
# - ValueError
# - FileNotFoundError
# - IndexError
# - TypeError
#
# ===============================================================================


# 1) Handle division by zero using try-except
def safe_division(a, b):
	try:
		result = a / b
		print(f"Result: {result}")
	except ZeroDivisionError:
		print("Error: Division by zero is not allowed")


# 2) Handle ValueError for non-numeric input
def convert_to_int(user_input):
	try:
		number = int(user_input)
		print(f"Valid integer entered: {number}")
	except ValueError:
		print("Error: Please enter a numeric value")


# 3) Handle multiple exceptions (ZeroDivisionError and ValueError)
def divide_user_inputs(value1, value2):
	try:
		num1 = float(value1)
		num2 = float(value2)
		result = num1 / num2
		print(f"Division result: {result}")
	except ValueError:
		print("Error: One or both inputs are not valid numbers")
	except ZeroDivisionError:
		print("Error: Cannot divide by zero")


# 4) Demonstrate finally block
def finally_demo(a, b):
	try:
		result = a / b
		print(f"Result: {result}")
	except ZeroDivisionError:
		print("Error: Division by zero")
	finally:
		# This line always executes.
		print("finally block executed (always runs)")


# 5) Handle file not found error
def read_file_safely(file_name):
	try:
		with open(file_name, "r", encoding="utf-8") as file:
			content = file.read()
			print("File content:")
			print(content)
	except FileNotFoundError:
		print(f"Error: File '{file_name}' not found")


# 6) Use try, except, else, and finally blocks
def complete_exception_flow(a, b):
	try:
		result = a / b
	except ZeroDivisionError:
		print("Error: Denominator cannot be zero")
	else:
		# Runs only if no exception occurred in try block.
		print(f"Division successful: {result}")
	finally:
		# Runs in both success and failure cases.
		print("Operation completed (finally block)")


# 7) Raise a custom exception using raise
class AgeTooSmallError(Exception):
	# Custom exception class for age validation.
	pass


def validate_age(age):
	if age < 18:
		raise AgeTooSmallError("Age must be 18 or above")
	print("Age is valid")


# 8) Handle IndexError when accessing list elements
def access_list_element(data_list, index):
	try:
		print(f"Element at index {index}: {data_list[index]}")
	except IndexError:
		print("Error: Index is out of range")


# 9) Handle TypeError for incompatible data types
def add_values(value1, value2):
	try:
		result = value1 + value2
		print(f"Addition result: {result}")
	except TypeError:
		print("Error: Incompatible data types for addition")


# 10) Validate user input and handle invalid entries
def validate_positive_integer(user_input):
	try:
		number = int(user_input)
		if number <= 0:
			raise ValueError("Number must be positive")
		print(f"Valid positive integer: {number}")
	except ValueError as error:
		print(f"Invalid input: {error}")


# ======================== TEST / OUTPUT SECTION ========================
if __name__ == "__main__":
	print("--- 1) Division by Zero Handling ---")
	safe_division(10, 0)
	safe_division(10, 2)
	print()

	print("--- 2) ValueError Handling ---")
	convert_to_int("25")
	convert_to_int("abc")
	print()

	print("--- 3) Multiple Exceptions ---")
	divide_user_inputs("20", "4")
	divide_user_inputs("20", "0")
	divide_user_inputs("abc", "4")
	print()

	print("--- 4) finally Block Demo ---")
	finally_demo(8, 2)
	finally_demo(8, 0)
	print()

	print("--- 5) File Not Found Handling ---")
	read_file_safely("sample.txt")
	print()

	print("--- 6) try-except-else-finally Demo ---")
	complete_exception_flow(12, 3)
	complete_exception_flow(12, 0)
	print()

	print("--- 7) Custom Exception using raise ---")
	try:
		validate_age(16)
	except AgeTooSmallError as custom_error:
		print(f"Custom Exception: {custom_error}")
	validate_age(22)
	print()

	print("--- 8) IndexError Handling ---")
	sample_list = [10, 20, 30]
	access_list_element(sample_list, 1)
	access_list_element(sample_list, 5)
	print()

	print("--- 9) TypeError Handling ---")
	add_values(10, 5)
	add_values("Hello", 10)
	print()

	print("--- 10) Input Validation with Exception Handling ---")
	validate_positive_integer("15")
	validate_positive_integer("-4")
	validate_positive_integer("xyz")
