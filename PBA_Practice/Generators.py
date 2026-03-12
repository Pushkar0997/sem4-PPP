# ======================== PYTHON GENERATORS - THEORY ========================
#
# What is a Generator?
# A generator is a special function that returns values one-by-one using 'yield'
# instead of returning all values at once.
#
# Why generators are useful:
# 1. Memory efficient: they do not store the full result list in memory.
# 2. Good for large data: useful for files, big ranges, streams, etc.
# 3. Lazy execution: next value is created only when needed.
#
# return vs yield:
# - return: ends the function and gives one final value.
# - yield: pauses the function, gives one value, and resumes from same point later.
#
# How to use a generator:
# - Define a function with 'yield'.
# - Call the function to get a generator object.
# - Iterate using a for-loop or next().
#
# ============================================================================


# ===== 1. Generator for first n Fibonacci numbers =====
def fibonacci_generator(n):
	# a = first Fibonacci number, b = second Fibonacci number
	a, b = 0, 1

	# count tracks how many numbers we have generated so far
	count = 0

	# Repeat until we generate n numbers
	while count < n:
		# Yield current Fibonacci number
		yield a

		# Update Fibonacci values:
		# new a becomes old b
		# new b becomes old a + old b
		a, b = b, a + b

		# Increase generated count by 1
		count += 1


# ===== 2. Generator for even numbers between two limits =====
def even_numbers_generator(start, end):
	# Loop from start to end (inclusive)
	for num in range(start, end + 1):
		# Check if number is even using modulo
		if num % 2 == 0:
			# Yield even number
			yield num


# ===== 3. Generator to read a large file line by line =====
def read_large_file(file_path):
	# Open file in read mode
	# with-block closes file automatically after reading is done
	with open(file_path, "r", encoding="utf-8") as file:
		# Read one line at a time from file
		for line in file:
			# Yield line after removing trailing newline/extra spaces
			yield line.strip()


# ===== 4. Generator for prime numbers up to a limit =====
def prime_generator(limit):
	# Check every number from 2 to limit (inclusive)
	for num in range(2, limit + 1):
		# Assume current number is prime
		is_prime = True

		# Try dividing num by all numbers from 2 to num-1
		for i in range(2, num):
			# If divisible, it is not prime
			if num % i == 0:
				is_prime = False
				# No need to check more divisors
				break

		# Yield number only if it is prime
		if is_prime:
			yield num


# ===== 5. Generator for countdown timer =====
def countdown_generator(start):
	# Continue until start reaches 0
	while start >= 0:
		# Yield current value
		yield start

		# Decrease by 1 for countdown
		start -= 1


# ===== Test Examples =====
if __name__ == "__main__":
	# ---------- 1) Fibonacci ----------
	print("First 10 Fibonacci numbers:")
	for value in fibonacci_generator(10):
		print(value, end=" ")
	print("\n")

	# ---------- 2) Even Numbers ----------
	print("Even numbers between 5 and 20:")
	for value in even_numbers_generator(5, 20):
		print(value, end=" ")
	print("\n")

	# ---------- 3) Read Large File ----------
	# Small demo file creation for testing this generator.
	# In real life, the same function works for very large files too.
	demo_file = "demo_lines.txt"
	with open(demo_file, "w", encoding="utf-8") as f:
		f.write("Line 1\n")
		f.write("Line 2\n")
		f.write("Line 3\n")

	print("Reading file line by line using generator:")
	for line in read_large_file(demo_file):
		print(line)
	print()

	# ---------- 4) Prime Numbers ----------
	print("Prime numbers up to 30:")
	for value in prime_generator(30):
		print(value, end=" ")
	print("\n")

	# ---------- 5) Countdown ----------
	print("Countdown from 5:")
	for value in countdown_generator(5):
		print(value, end=" ")
	print()

