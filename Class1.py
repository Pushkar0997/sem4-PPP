# def deco1(funct):
#     def wrapper():
#         print("Welcome")
#         funct()
#         print("Thanks for for coming")
#     return wrapper

# @deco1

# def batch2(a,b):
#     print(f"the sum of {a} and {b} is {a+b}")

# batch2(5,6)

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
    
result = calculator(10, 5, "add")
print("Result:", result)

# Implement a decorator that logs the function name and arguments whenever the function is called.

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
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

result = calculator(10, 5, "multiply")
print("Result:", result)

# Create a decorator that measures the execution time of a function and prints it.

def measure_time(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of '{func.__name__}': {end_time - start_time} seconds")
        return result
    return wrapper

@measure_time
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

# write a program that pauses the execution for a specified number of seconds using sleep().

def pause_execution(seconds):
    import time
    print(f"Pausing execution for {seconds} seconds...")
    time.sleep(seconds)
    print("Resuming execution.")

pause_execution(3)

# write a program to display the current date and time of the system.

def display_current_datetime():
    from datetime import datetime
    now = datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()

# create a digital 