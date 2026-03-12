# ================= DECORATORS + GENERATORS + TIME (ADVANCED BASICS) =================
#
# This file combines three ideas:
# 1. Decorators: wrap functions to add extra behavior (timing, delay, logging)
# 2. Generators: produce values one-by-one using yield
# 3. time module: current time, sleep delays, and execution timing
#
# Why combine them?
# - Very useful in real projects (logging, streaming data, monitoring performance)
# - Keeps code clean: business logic stays simple, decorator adds common features
#
# ================================================================================

import time


# ===== 1) Decorator to calculate and display execution time of a generator function =====
def time_generator_execution(func):
	# This decorator assumes the decorated function returns a generator.
	def wrapper(*args, **kwargs):
		# Record start time before generator consumption starts.
		start = time.time()

		# Create generator object from original function.
		gen = func(*args, **kwargs)

		# Yield each value from the original generator one by one.
		# We use this loop so timing includes full consumption duration.
		for value in gen:
			yield value

		# When generator is fully exhausted, record end time.
		end = time.time()

		# Print total time taken to produce all generated values.
		print(f"Generator '{func.__name__}' execution time: {end - start:.6f} seconds")

	return wrapper


# ===== 2) Decorator that delays function execution by 3 seconds =====
def delay_by_3_seconds(func):
	# This decorator adds a fixed delay before calling the function.
	def wrapper(*args, **kwargs):
		# Inform user that delay is happening.
		print(f"Delaying '{func.__name__}' by 3 seconds...")

		# Pause execution for 3 seconds.
		time.sleep(3)

		# Call and return original function result.
		return func(*args, **kwargs)

	return wrapper


# ===== 3) Generator that produces timestamps at regular intervals =====
def timestamp_generator(interval_seconds, count):
	# Generate 'count' timestamps with fixed interval.
	for _ in range(count):
		# time.strftime() converts current local time to readable text.
		timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

		# Yield current timestamp.
		yield timestamp

		# Wait for interval before next timestamp.
		time.sleep(interval_seconds)


# ===== 4) Decorator that logs execution time and function name =====
def log_execution_details(func):
	# This decorator can be reused on many different functions.
	def wrapper(*args, **kwargs):
		# Start timer.
		start = time.time()

		# Execute original function.
		result = func(*args, **kwargs)

		# End timer.
		end = time.time()

		# Log function name and execution duration.
		print(f"Function: {func.__name__} | Time: {end - start:.6f} seconds")

		# Return original result unchanged.
		return result

	return wrapper


# ===== 5) Generator to simulate real-time sensor data with time delays =====
def sensor_data_generator(total_readings, delay_seconds=1):
	# Produce sensor-like data one reading at a time.
	# Here we use a simple numeric pattern as fake sensor value.
	for reading_no in range(1, total_readings + 1):
		# Fake sensor value changes with reading number.
		sensor_value = 20 + reading_no * 0.5

		# Include reading id, timestamp, and value in dictionary format.
		data = {
			"reading": reading_no,
			"time": time.strftime("%H:%M:%S", time.localtime()),
			"value": sensor_value,
		}

		# Yield one sensor packet.
		yield data

		# Wait before producing next packet (real-time simulation).
		time.sleep(delay_seconds)


# =========================== Demo Functions for Testing ===========================

@time_generator_execution
def fibonacci_with_delay(n):
	# Simple Fibonacci generator with small delay to show timing clearly.
	a, b = 0, 1
	for _ in range(n):
		yield a
		a, b = b, a + b
		time.sleep(0.2)


@delay_by_3_seconds
def say_hello(name):
	# Simple function used to test delay decorator.
	print(f"Hello, {name}!")


@log_execution_details
def add_numbers(a, b):
	# Sample function 1 for logging decorator.
	time.sleep(0.5)
	return a + b


@log_execution_details
def multiply_numbers(a, b):
	# Sample function 2 for logging decorator.
	time.sleep(0.3)
	return a * b


# =================================== Test Block ===================================
if __name__ == "__main__":
	# 1) Timing a generator function using decorator.
	print("--- 1) Timed Generator (Fibonacci) ---")
	for num in fibonacci_with_delay(5):
		print(num, end=" ")
	print("\n")

	# 2) Delaying function execution by 3 seconds.
	print("--- 2) Delay Decorator ---")
	say_hello("Pushkar")
	print()

	# 3) Timestamp generator at regular intervals.
	print("--- 3) Timestamp Generator (every 1 second) ---")
	for ts in timestamp_generator(interval_seconds=1, count=3):
		print("Timestamp:", ts)
	print()

	# 4) Logging execution details for multiple functions.
	print("--- 4) Log Function Name + Execution Time ---")
	sum_result = add_numbers(10, 20)
	print("add_numbers result:", sum_result)
	product_result = multiply_numbers(4, 5)
	print("multiply_numbers result:", product_result)
	print()

	# 5) Real-time sensor data simulation with generator + delay.
	print("--- 5) Sensor Data Generator ---")
	for packet in sensor_data_generator(total_readings=5, delay_seconds=1):
		print(packet)
