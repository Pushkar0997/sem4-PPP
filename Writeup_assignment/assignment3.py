"""
Experiment No: 3

Title:
Write a Python program using filter, map, reduce, and lambda to process a list
of words. Filter words with length > 4, convert them to lowercase using map,
and use reduce to join the processed words into a single sentence.

Aim:
To write a Python program using filter, map, reduce, and lambda functions to
process a list of user-provided words.

Objective:
- Learn how to take user input in Python.
- Apply filter() to select words based on length.
- Use map() to transform text.
- Use reduce() to combine elements.
- Understand lambda functions in functional programming.

Theory:
Functional Programming with User Input:
- filter() selects elements that meet a condition.
- map() transforms each element.
- reduce() combines elements into one result.
- lambda provides short, anonymous functions.

In this program:
- The user enters words as a sentence.
- The sentence is split into a list.
- Words with length > 4 are filtered.
- Words are converted to lowercase.
- The processed words are joined into a single sentence.
"""

from functools import reduce


try:
    text = input("Enter words: ").strip()

    if text == "":
        raise ValueError("Input cannot be empty")

    words = text.split()

    filtered_words = list(filter(lambda w: len(w) > 4, words))
    lowercase_words = list(map(lambda w: w.lower(), filtered_words))

    if len(lowercase_words) == 0:
        raise ValueError("No word found with length greater than 4")

    sentence = reduce(lambda a, b: a + " " + b, lowercase_words)

    print("Processed sentence:", sentence)

except ValueError as error:
    print("Error:", error)


# Expected Output (example 1):
# Enter words: Hello This is PYTHON Programming Class
# Processed sentence: hello python programming class

# Expected Output (example 2):
# Enter words: I am in lab
# Error: No word found with length greater than 4


"""
Conclusion:
- Successfully processed user input using functional programming tools.
- Used filter(), map(), and reduce() together in a pipeline.
- Demonstrated lambda expressions for concise operations.
- Implemented error handling for invalid cases.
- Improved understanding of dynamic data processing.

Frequently Asked Questions (FAQs):

1. Why use split() on user input?
	split() breaks the input sentence into individual words. This lets us apply
	filter(), map(), and reduce() on each word easily.

2. What if no word is longer than 4 characters?
	Then the filtered list becomes empty. In this program, we raise a ValueError
	and show a clear message instead of giving a wrong result.

3. Why use try-except here?
	try-except handles invalid cases such as empty input or no matching words.
	It keeps the program from crashing and shows user-friendly errors.

4. Can we use join() instead of reduce()?
	Yes, " ".join(words) is simpler and commonly used for joining strings.
	Here we use reduce() because the experiment specifically asks for it.

5. Can this work with numbers?
	Yes, if numbers are entered as text, they are treated like normal words.
	The length check still works on their string form.

6. What is a lambda function in Python?
	A lambda function is a small anonymous function written in one line.
	It is useful for short operations inside filter(), map(), and reduce().

7. Why do we import reduce from functools?
	In Python 3, reduce() is not a built-in function.
	It is available in the functools module, so we import it from there.

8. Can reduce() be replaced with join()?
	Yes, for joining strings, join() is generally cleaner and faster.
	reduce() is used here for learning functional programming concepts.
"""
