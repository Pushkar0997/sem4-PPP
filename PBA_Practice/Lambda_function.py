# ======================== PYTHON lambda FUNCTION - THEORY ========================
#
# What is a lambda function?
# A lambda function is a small anonymous (nameless) function in one line.
#
# Syntax:
# lambda arguments: expression
#
# Example:
# lambda a, b: a + b
#
# Why use lambda?
# 1) Short and quick function definition.
# 2) Useful for simple operations.
# 3) Commonly used with map(), filter(), sorted(), etc.
#
# ===============================================================================


# 1) Lambda function that adds two numbers
add_two_numbers = lambda a, b: a + b


# 2) Lambda function to find square of a number
square_number = lambda x: x * x


# 3) Lambda to check whether number is even or odd
# If remainder when divided by 2 is 0 -> Even, otherwise Odd.
check_even_odd = lambda n: "Even" if n % 2 == 0 else "Odd"


# 4) Lambda function to find maximum of two numbers
max_of_two = lambda a, b: a if a > b else b


# 5) Lambda function to multiply two numbers
multiply_two_numbers = lambda a, b: a * b


# 6) Lambda function to calculate cube of a number
cube_number = lambda x: x ** 3


# ======================== TEST / OUTPUT SECTION ========================
if __name__ == "__main__":
	print("--- 1) Add Two Numbers ---")
	print("add_two_numbers(10, 20) =", add_two_numbers(10, 20))
	print()

	print("--- 2) Square of a Number ---")
	print("square_number(6) =", square_number(6))
	print()

	print("--- 3) Check Even or Odd ---")
	print("check_even_odd(12) =", check_even_odd(12))
	print("check_even_odd(7) =", check_even_odd(7))
	print()

	print("--- 4) Maximum of Two Numbers ---")
	print("max_of_two(45, 60) =", max_of_two(45, 60))
	print()

	print("--- 5) Multiply Two Numbers ---")
	print("multiply_two_numbers(8, 5) =", multiply_two_numbers(8, 5))
	print()

	print("--- 6) Cube of a Number ---")
	print("cube_number(4) =", cube_number(4))
