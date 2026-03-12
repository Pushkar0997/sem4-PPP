# ===== 1. Function to find sum of all elements in a list =====
def sum_of_list(numbers):
    # Initialize total to 0 (stores the sum)
    total = 0
    # Loop through each number in the list
    for num in numbers:
        # Add current number to total using += operator
        total += num
    # Return the final sum
    return total


# ===== 2. Function to check if a number is even or odd =====
def check_even_odd(number):
    # If number divided by 2 has remainder 0, it is even
    if number % 2 == 0:
        # Return "Even" if condition is true
        return "Even"
    # If remainder is not 0, number is odd
    else:
        # Return "Odd" if number is not divisible by 2
        return "Odd"


# ===== 3. Function to find maximum of three numbers =====
def max_of_three(a, b, c):
    # Assume first number is the maximum
    max_num = a
    # Compare second number with current maximum
    if b > max_num:
        # Update maximum if b is greater
        max_num = b
    # Compare third number with current maximum
    if c > max_num:
        # Update maximum if c is greater
        max_num = c
    # Return the maximum number found
    return max_num


# ===== 4. Function to count vowels in a string =====
def count_vowels(string):
    # Convert string to lowercase to match all vowels
    string = string.lower()
    # Initialize vowel count to 0
    vowel_count = 0
    # Define all vowels in a string
    vowels = "aeiou"
    # Loop through each character in the string
    for char in string:
        # Check if character is a vowel
        if char in vowels:
            # Increment vowel count by 1
            vowel_count = vowel_count + 1
    # Return total count of vowels
    return vowel_count


# ===== 5. Function to check if a number is prime =====
def is_prime(number):
    # Prime numbers must be greater than 1
    if number <= 1:
        # Return False if number is 1 or less
        return False
    # Check divisors from 2 to number-1
    for i in range(2, number):
        # If number is divisible by i, it is not prime
        if number % i == 0:
            # Return False when divisor is found
            return False
    # If no divisor found, number is prime
    return True


# ===== 6. Function to convert temperature Celsius to Fahrenheit and vice versa =====
def celsius_to_fahrenheit(celsius):
    # Formula: F = (C * 9/5) + 32
    # Multiply celsius by 9/5 (or 1.8)
    fahrenheit = (celsius * 9/5) + 32
    # Return temperature in Fahrenheit
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    # Formula: C = (F - 32) * 5/9
    # Subtract 32 from fahrenheit, then multiply by 5/9
    celsius = (fahrenheit - 32) * 5/9
    # Return temperature in Celsius
    return celsius


# ===== 7. Function to count words in a sentence =====
def count_words(sentence):
    # Use split() which splits string by spaces into a list of words
    words = sentence.split()
    # Get length of the words list
    word_count = len(words)
    # Return the count of words
    return word_count


# ===== 8. Function to validate password =====
def validate_password(password):
    # Check if password length is at least 8 characters
    if len(password) < 8:
        # Return False if password is too short
        return False
    
    # Initialize flags to track if requirements are met
    has_digit = False
    has_special = False
    
    # Define special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Loop through each character in password
    for char in password:
        # Check if character is a digit (0-9)
        if char.isdigit():
            # Set flag to True if digit found
            has_digit = True
        # Check if character is a special character
        if char in special_chars:
            # Set flag to True if special character found
            has_special = True
    
    # Check if all requirements are met (length >= 8, has digit, has special char)
    if has_digit and has_special:
        # Return True if all conditions satisfied
        return True
    # Return False if any requirement is not met
    return False


# ===== 9. Simple Calculator Function =====
def calculator(num1, num2, operation):
    # Check what operation user wants to perform
    # If operation is addition
    if operation == "+":
        # Add both numbers and return result
        return num1 + num2
    # If operation is subtraction
    elif operation == "-":
        # Subtract num2 from num1 and return result
        return num1 - num2
    # If operation is multiplication
    elif operation == "*":
        # Multiply both numbers and return result
        return num1 * num2
    # If operation is division
    elif operation == "/":
        # Check if num2 is 0 to avoid division by zero
        if num2 == 0:
            # Return error message if trying to divide by zero
            return "Error: Cannot divide by zero"
        # Divide num1 by num2 and return result
        return num1 / num2
    # If operation is not recognized
    else:
        # Return error message for invalid operation
        return "Error: Invalid operation"


# ===== Test Examples =====
if __name__ == "__main__":
    # Testing sum_of_list function
    print("Sum:", sum_of_list([1, 2, 3, 4, 5]))
    
    # Testing check_even_odd function
    print("12 is:", check_even_odd(12))
    print("7 is:", check_even_odd(7))
    
    # Testing max_of_three function
    print("Max of 10, 20, 15:", max_of_three(10, 20, 15))
    
    # Testing count_vowels function
    print("Vowels in 'Hello World':", count_vowels("Hello World"))
    
    # Testing is_prime function
    print("Is 7 prime?:", is_prime(7))
    print("Is 10 prime?:", is_prime(10))
    
    # Testing temperature conversion
    print("25°C in Fahrenheit:", celsius_to_fahrenheit(25))
    print("77°F in Celsius:", fahrenheit_to_celsius(77))
    
    # Testing count_words function
    print("Words in sentence:", count_words("Python is awesome"))
    
    # Testing validate_password function
    print("Password 'Pass@123' valid?:", validate_password("Pass@123"))
    print("Password 'weak' valid?:", validate_password("weak"))
    
    # Testing calculator function
    print("10 + 5 =", calculator(10, 5, "+"))
    print("10 - 5 =", calculator(10, 5, "-"))
    print("10 * 5 =", calculator(10, 5, "*"))
    print("10 / 5 =", calculator(10, 5, "/"))
