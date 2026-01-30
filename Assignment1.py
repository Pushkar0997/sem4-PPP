# Write a Python program to create a custom decorator that logs the name and execution time of a function.

import time

def log_and_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of '{func.__name__}': {end_time - start_time} seconds")
        return result
    return wrapper

@log_and_time
def calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
    
result = calculator(10, 5, "subtract")
print("Result:", result)