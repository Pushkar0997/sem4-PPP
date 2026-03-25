"""
Experiment No: 2

Title:
Implement a Python class to manage student records, demonstrating inheritance
and basic error handling for invalid inputs.

Aim:
To implement a Python class for managing student records while demonstrating
inheritance and basic error handling for invalid inputs.

Objective:
- Learn how to create and manage student records using classes in Python.
- Demonstrate the concept of inheritance by creating a base and derived class.
- Implement basic error handling to ensure data validity.
- Understand how encapsulation and method overriding work in OOP.

Theory:
Object-Oriented Programming (OOP) in Python:
- Encapsulation: Restricts direct access to variables by using methods.
- Inheritance: Allows a class to reuse properties and methods of another class.
- Polymorphism: Allows child classes to override parent methods.

Error Handling in Python:
- try-except blocks handle invalid data and prevent program crashes.
- We validate student name, age, and grade to avoid wrong records.
"""


class Person:
	def __init__(self, name, age):
		if not name.strip():
			raise ValueError("Name cannot be empty")
		if age <= 0:
			raise ValueError("Age must be greater than 0")

		self._name = name
		self._age = age

	def get_name(self):
		return self._name

	def get_age(self):
		return self._age

	def display_info(self):
		print(f"Name: {self._name}, Age: {self._age}")


class Student(Person):
	def __init__(self, name, age, roll_no, grade):
		super().__init__(name, age)

		if not roll_no.strip():
			raise ValueError("Roll number cannot be empty")
		if grade < 0 or grade > 100:
			raise ValueError("Grade must be between 0 and 100")

		self._roll_no = roll_no
		self._grade = grade

	# Method overriding: this replaces the parent display format.
	def display_info(self):
		print(
			f"Name: {self._name}, Age: {self._age}, "
			f"Roll No: {self._roll_no}, Grade: {self._grade}"
		)


if __name__ == "__main__":
	try:
		student1 = Student("Rahul", 20, "S101", 88)
		student1.display_info()

		# Invalid input example (age is negative)
		student2 = Student("Anita", -2, "S102", 75)
		student2.display_info()

	except ValueError as error:
		print("Error:", error)


# Expected Output (example):
# Name: Rahul, Age: 20, Roll No: S101, Grade: 88
# Error: Age must be greater than 0


"""
Conclusion:
- Successfully implemented a Python class hierarchy for student records.
- Demonstrated inheritance by extending Person into Student.
- Implemented error handling using try-except for invalid inputs.
- Overrode display_info() in the Student class.

Frequently Asked Questions (FAQs):

1. What is inheritance in Python?
   Inheritance allows one class to use properties and methods of another class.
   It helps reduce repeated code and supports better code organization.

2. How does method overriding work?
   Method overriding means defining a method in the child class with the same
   name as in the parent class. When called on the child object, the child
   method runs instead of the parent version.

3. Why use error handling in this program?
   Error handling prevents the program from crashing on invalid data.
   It also shows clear error messages so users can correct their inputs.

4. Can we add more attributes to the Student class?
   Yes, we can add fields like email, phone, or department easily.
   We should also validate new fields to keep data accurate.

5. How can we improve this program?
   We can store multiple students in a list or file/database for real usage.
   We can also add update, delete, and search functions for better management.
"""
