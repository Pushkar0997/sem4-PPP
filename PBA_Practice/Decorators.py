# ======================== PYTHON DECORATORS - THEORY ========================
#
# What is a Decorator?
# A decorator is a function that:
#   1. Takes another function as input (as a parameter)
#   2. Adds new functionality or modifies the behavior of that function
#   3. Returns a new function that replaces the original function
# Key idea: Decorators let you "wrap" a function without changing its code!
#
# Why Use Decorators?
# - Add features like logging, timing, authentication without changing original code
# - Keep your code DRY (Don't Repeat Yourself)
# - Separate concerns (original logic vs. extra features)
#
# Key Concepts You Must Know:
#
# 1. FUNCTIONS ARE FIRST-CLASS OBJECTS
#    In Python, functions are objects that can be:
#    - Assigned to variables: my_var = my_function
#    - Passed as arguments: other_function(my_function)
#    - Returned from functions: return my_function
#
# 2. CLOSURES
#    A closure is when a function "remembers" variables from its parent scope
#    Example: The wrapper() function inside a decorator remembers 'func'
#    even after the decorator() function has finished executing
#
# 3. THE @ SYNTAX (SYNTACTIC SUGAR)
#    @decorator_name
#    def my_function():
#        pass
#    
#    This is EXACTLY the same as:
#    def my_function():
#        pass
#    my_function = decorator_name(my_function)
#
# 4. *args and **kwargs
#    *args = tuple of positional arguments (non-keyword arguments)
#    **kwargs = dictionary of keyword arguments
#    These allow decorator to work with ANY function signature
#
# How Decorators Work (Simple 4-Step Process):
# Step 1: Create a decorator function that accepts a function parameter
# Step 2: Inside decorator, define a wrapper function
# Step 3: Wrapper does "before" logic, calls original function, does "after" logic
# Step 4: Decorator returns the wrapper function
#
# ============================================================================


# ===== 1. Decorator that prints message before and after function execution =====
def message_decorator(func):
    # Parameter 'func' will receive the function we want to decorate
    # Example: if we use @message_decorator above a function,
    # that entire function object is passed here as 'func'
    
    # Define an inner function called wrapper
    # This wrapper will be called instead of the original function
    # *args captures any positional arguments (like message_decorator(1, 2, 3))
    # **kwargs captures any keyword arguments (like message_decorator(name="John"))
    def wrapper(*args, **kwargs):
        # THIS RUNS BEFORE THE ORIGINAL FUNCTION EXECUTES
        print("Function is about to execute")
        
        # Call the original function using 'func' variable
        # Pass all arguments to it using *args, **kwargs
        result = func(*args, **kwargs)
        
        # THIS RUNS AFTER THE ORIGINAL FUNCTION EXECUTES
        print("Function execution completed")
        
        # Return the result from the original function (unchanged)
        return result
    
    # Return the wrapper function
    # Now when someone calls the decorated function, they're actually calling wrapper
    return wrapper


# ===== 2. Decorator that measures and displays execution time =====
import time

def timer_decorator(func):
    # Parameter 'func' receives the function being decorated
    
    def wrapper(*args, **kwargs):
        # STEP 1: Record the time BEFORE executing the function
        # time.time() returns current time as seconds since January 1, 1970
        start_time = time.time()
        
        # STEP 2: Call the original function with all its arguments
        # This is where the actual function code runs
        result = func(*args, **kwargs)
        
        # STEP 3: Record the time AFTER the function executes
        end_time = time.time()
        
        # STEP 4: Calculate how many seconds the function took
        # Subtract start time from end time to get duration
        execution_time = end_time - start_time
        
        # STEP 5: Print the timing info to console
        # func.__name__ gets the original function's name as a string
        # :.4f formats the number with 4 decimal places
        # Example output: "Function 'my_func' took 0.5678 seconds"
        print(f"Function '{func.__name__}' took {execution_time:.4f} seconds")
        
        # STEP 6: Return the result unchanged
        return result
    
    # Return the wrapper so it replaces the original function
    return wrapper


# ===== 3. Decorator to restrict function execution if user is not authenticated =====
def authentication_decorator(func):
    # Parameter 'func' receives the function being decorated
    
    def wrapper(*args, **kwargs):
        # This variable checks if the user is authenticated
        # In real applications, this would check:
        # - Database for user credentials
        # - Session/cookies from web request
        # - JWT tokens, etc.
        # For this example, it's hardcoded to True for testing
        is_authenticated = True
        
        # Check the authentication status
        if is_authenticated:
            # If the user IS authenticated, allow the function to execute
            # Call the original function normally
            result = func(*args, **kwargs)
            # Return its result
            return result
        
        # If user is NOT authenticated (else block)
        else:
            # Don't execute the function at all
            # Print an error message instead
            print("Error: User is not authenticated. Access denied!")
            # Return None instead of executing the protected function
            return None
    
    # Return the wrapper that now protects the original function
    return wrapper


# ===== 4. Decorator that logs function name and arguments =====
def logging_decorator(func):
    # Parameter 'func' receives the function being decorated
    
    def wrapper(*args, **kwargs):
        # Get the name of the original function as a string
        # Every function in Python has a __name__ attribute
        # Example: if decorating function 'add', func.__name__ = "add"
        function_name = func.__name__
        
        # Print which function was called
        # This is useful for debugging and tracking code flow
        print(f"Function called: {function_name}")
        
        # Print all the positional arguments
        # args is a tuple (immutable list) of all positional arguments
        # Example: if function is called as add(5, 10), args = (5, 10)
        print(f"Arguments: {args}")
        
        # Print all the keyword arguments
        # kwargs is a dictionary of all keyword arguments
        # Example: if function is called as add(a=5, b=10), kwargs = {'a': 5, 'b': 10}
        print(f"Keyword Arguments: {kwargs}")
        
        # Now call the original function with all its arguments
        # When positional and keyword arguments are passed together,
        # *args unpacks tuple to positional args, **kwargs unpacks dict to keyword args
        result = func(*args, **kwargs)
        
        # Return the result from the original function
        return result
    
    # Return the wrapper that now logs all function calls
    return wrapper


# ===== 5. Decorator that counts how many times a function has been invoked =====
def counter_decorator(func):
    # Parameter 'func' receives the function being decorated
    
    # Attach a counter attribute directly to the function object
    # In Python, functions are objects and can have attributes attached
    # This counter will PERSIST between function calls (it remembers the value!)
    # This is an example of a closure - the wrapper remembers this value
    func.call_count = 0
    
    def wrapper(*args, **kwargs):
        # Increment (increase by 1) the counter each time the function is called
        # += means "add to current value" (func.call_count = func.call_count + 1)
        # The counter increases with EVERY call to this function
        func.call_count += 1
        
        # Call the original function with all its arguments
        result = func(*args, **kwargs)
        
        # Print how many times this function has been called TOTAL
        # func.__name__ is the function's name
        # func.call_count is the number from our counter we incremented above
        # Example output: "Function 'my_func' has been called 3 times"
        print(f"Function '{func.__name__}' has been called {func.call_count} times")
        
        # Return the result from the original function
        return result
    
    # Return the wrapper that now counts function invocations
    return wrapper


# ===== Test Examples (Demonstrating How Decorators Work) =====
if __name__ == "__main__":
    # ===== Testing message_decorator =====
    print("--- Testing message_decorator ---")
    
    # The @ syntax applies the decorator to the function
    # @message_decorator is EQUIVALENT to:
    #   def greet(name):
    #       print(f"Hello, {name}!")
    #   greet = message_decorator(greet)
    @message_decorator
    def greet(name):
        # This function is now "wrapped" by message_decorator
        print(f"Hello, {name}!")
    
    # When we call greet(), we're actually calling the wrapper() function
    # Wrapper executes:
    #   1. "Function is about to execute" (before logic)
    #   2. The original greet() function
    #   3. "Function execution completed" (after logic)
    greet("Alice")
    
    
    # ===== Testing timer_decorator =====
    print("\n--- Testing timer_decorator ---")
    
    # This decorator measures how long the function takes to execute
    @timer_decorator
    def slow_function():
        # time.sleep() pauses execution for the given seconds
        # This simulates a slow/heavy function for testing timing
        time.sleep(1)
        # Print a message when function finishes
        print("Function completed")
    
    # When we call slow_function(), the wrapper:
    #   1. Records start time
    #   2. Calls original function (sleeps for 1 second)
    #   3. Records end time
    #   4. Prints how many seconds it took
    slow_function()
    
    
    # ===== Testing authentication_decorator =====
    print("\n--- Testing authentication_decorator ---")
    
    # This decorator protects functions from running without authentication
    @authentication_decorator
    def access_data():
        # This sensitive function only runs if authenticated
        print("Accessing sensitive data...")
    
    # When we call access_data(), the wrapper:
    #   1. Checks if user is authenticated
    #   2. Only executes the function if authenticated is True
    #   3. Denies access if authentication fails
    access_data()
    
    
    # ===== Testing logging_decorator =====
    print("\n--- Testing logging_decorator ---")
    
    # This decorator logs (records) every time the function is called
    @logging_decorator
    def add(a, b):
        # Simple addition function
        # The decorator logs which function this is and what arguments were passed
        result = a + b
        # Print the result
        print(f"Result: {result}")
        # Return the sum
        return result
    
    # When we call add(5, 10), the wrapper:
    #   1. Logs the function name: "add"
    #   2. Logs positional arguments: (5, 10)
    #   3. Logs keyword arguments: (empty in this case)
    #   4. Executes the original function
    #   5. Returns the result
    add(5, 10)
    
    
    # ===== Testing counter_decorator =====
    print("\n--- Testing counter_decorator ---")
    
    # This decorator counts how many times a function has been called
    @counter_decorator
    def increment():
        # This function does some work
        print("Incrementing...")
    
    # Each call to increment() will show the total number of times it's been called
    # First call: increment() -> "has been called 1 times"
    print("First call:")
    increment()
    
    # Second call: increment() -> "has been called 2 times"
    print("Second call:")
    increment()
    
    # Third call: increment() -> "has been called 3 times"
    print("Third call:")
    increment()
    
    # Notice how the counter keeps track across multiple calls!
    # This works because of CLOSURE - the wrapper remembers func.call_count
