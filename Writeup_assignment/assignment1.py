"""
Experiment No: 1

Title:
Write a Python program to create a custom decorator that logs the name and
execution time of a function.

Aim:
To write a Python program that creates a custom decorator to log the name and
execution time of a function.

Objective:
- Understand the concept of Python decorators.
- Learn how to measure function execution time using the time module.
- Implement a logging mechanism for function execution details.

Theory:
A decorator in Python is a higher-order function that takes another function as
input and extends its behavior without modifying its original structure.
Python provides built-in decorators such as @staticmethod, @classmethod, and
@property.

In this program, we create a custom decorator that logs:
- The function name.
- The time taken to execute the function.

To achieve this, we use:
- The time module to measure execution time.
- A simple wrapper function inside the decorator.
- The @decorator syntax to apply it directly on a function.
"""

import time


def log_time(func):
  def wrapper():
    start_time = time.time()
    func()
    end_time = time.time()

    print(f"Function: {func.__name__}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")

  return wrapper


@log_time
def sample_task():
  time.sleep(1)
  print("Task completed")


if __name__ == "__main__":
  sample_task()


# Expected Output (example):
# Task completed
# Function: sample_task
# Execution time: 1.000123 seconds


"""
Conclusion:
- We successfully implemented a Python decorator to log the function name and
  execution time.
- This approach is useful for performance analysis and debugging.
- The decorator works generically for any function, making it reusable across
  multiple functions.

Frequently Asked Questions:

1. What is a Python decorator?
	A Python decorator is a function that takes another function and adds extra
	behavior to it without changing its original code. It helps keep code clean
	by separating reusable logic like logging, timing, or access control.

2. Why use a decorator for logging execution time?
	A decorator lets us add timing logic once and reuse it for many functions.
	This avoids repeating the same timing code and makes programs easier to
	maintain.

3. How does the time.time() function help in measuring execution time?
	time.time() returns the current time in seconds as a floating-point number.
	By subtracting start time from end time, we get the total execution duration
	of the function.

4. Why do we use functools.wraps(func) inside the decorator?
  functools.wraps(func) preserves the wrapped function's metadata (like name,
  docstring, and signature), which helps with debugging, introspection, and
  tools that rely on accurate function information.

5. Can we use this decorator for any function?
  Yes, decorators can be written for almost any function.
  This basic version handles only no-argument functions; using *args,
  **kwargs, and returning the result makes it broadly reusable.
"""
