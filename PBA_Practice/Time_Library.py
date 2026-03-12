# ======================== PYTHON TIME MODULE - THEORY ========================
#
# What is the time module?
# The built-in 'time' module provides functions to work with:
# - current system time
# - delays (sleep)
# - formatting date/time into readable text
# - measuring how long code takes to run
#
# Important functions used below:
# 1. time.time()      -> current time in seconds (Unix timestamp)
# 2. time.sleep(sec)  -> pauses program for given seconds
# 3. time.localtime() -> current local date/time as structured object
# 4. time.strftime()  -> formats time into readable string
#
# ============================================================================

import time


# ===== 1. Display current system time using time module =====
def show_current_system_time():
	# time.time() returns current system time as seconds since Jan 1, 1970
	current_time = time.time()

	# Print raw timestamp value
	print("Current system time (timestamp):", current_time)


# ===== 2. Measure execution time of a function =====
def measure_execution_time(func, *args, **kwargs):
	# Record start time before function call
	start = time.time()

	# Call the function with provided arguments
	result = func(*args, **kwargs)

	# Record end time after function call
	end = time.time()

	# Calculate total execution duration
	duration = end - start

	# Display how long the function took
	print(f"Execution time of '{func.__name__}': {duration:.6f} seconds")

	# Return original function result
	return result


# ===== 3. Pause execution using sleep() =====
def pause_for_seconds(seconds):
	# Print message before pausing
	print(f"Pausing program for {seconds} seconds...")

	# Pause execution for given seconds
	time.sleep(seconds)

	# Print message after pause ends
	print("Pause complete.")


# ===== 4. Digital clock that updates every second =====
def digital_clock(duration_seconds=10):
	# Run clock for a limited duration so demo ends automatically
	# duration_seconds = how long clock should run
	for _ in range(duration_seconds):
		# Get current local time
		now = time.localtime()

		# Format time as HH:MM:SS
		current_clock = time.strftime("%H:%M:%S", now)

		# Print current time on same line (\r moves cursor to line start)
		print("Digital Clock:", current_clock, end="\r")

		# Wait 1 second before next update
		time.sleep(1)

	# Move to next line after clock loop ends
	print()


# ===== 5. Display local time in human-readable format =====
def show_local_time_readable():
	# Get local time structure
	local = time.localtime()

	# Convert local time to readable format
	# %A = day name, %d = date, %B = month name, %Y = year
	# %I = hour (12-hour), %M = minute, %S = second, %p = AM/PM
	readable_time = time.strftime("%A, %d %B %Y - %I:%M:%S %p", local)

	# Print final human-readable local time
	print("Local time (readable):", readable_time)


# ===== Example function for timing demo =====
def sample_work():
	# Simple loop to consume some time
	total = 0
	for i in range(1, 100000):
		total += i
	return total


# ===== Test Examples =====
if __name__ == "__main__":
	# 1) Current system time
	print("--- 1) Current System Time ---")
	show_current_system_time()
	print()

	# 2) Measure execution time
	print("--- 2) Measure Execution Time ---")
	result = measure_execution_time(sample_work)
	print("Sample function result:", result)
	print()

	# 3) Pause using sleep
	print("--- 3) Pause Execution ---")
	pause_for_seconds(2)
	print()

	# 4) Digital clock
	print("--- 4) Digital Clock (runs for 5 seconds) ---")
	digital_clock(duration_seconds=5)
	print()

	# 5) Human-readable local time
	print("--- 5) Human-Readable Local Time ---")
	show_local_time_readable()

