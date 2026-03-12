# ======================== PYTHON ENCAPSULATION - THEORY ========================
#
# What is Encapsulation?
# Encapsulation means wrapping data (variables) and methods (functions)
# together in one class, and controlling how data is accessed.
#
# Access levels in Python (by naming convention):
# 1) Public variable    -> normal name (example: name)
#    - Accessible from anywhere.
#
# 2) Protected variable -> single underscore (example: _salary)
#    - Should be used only inside class and subclass.
#    - Still accessible outside, but treated as "internal use".
#
# 3) Private variable   -> double underscore (example: __balance)
#    - Python does name mangling to prevent direct outside access.
#    - Best for sensitive data.
#
# Why encapsulation?
# - Data hiding for security.
# - Validation before updating data.
# - Better control and cleaner design.
#
# ============================================================================


# ================= 1) BANK ACCOUNT SECURITY SYSTEM (PRIVATE) =================
class BankAccount:
	# Constructor initializes private balance.
	def __init__(self, initial_balance=0):
		# Private variable: cannot be accessed directly as obj.__balance.
		self.__balance = initial_balance

	def deposit(self, amount):
		# Validate deposit amount.
		if amount > 0:
			self.__balance += amount
			print(f"Deposited: {amount}")
		else:
			print("Deposit amount must be greater than 0")

	def withdraw(self, amount):
		# Validate withdrawal amount and available balance.
		if amount <= 0:
			print("Withdrawal amount must be greater than 0")
		elif amount > self.__balance:
			print("Insufficient balance")
		else:
			self.__balance -= amount
			print(f"Withdrawn: {amount}")

	def get_balance(self):
		# Authorized method to view private balance.
		return self.__balance


# ============== 2) EMPLOYEE PAYROLL SYSTEM (PROTECTED + INHERITANCE) ==============
class Employee:
	# Constructor initializes protected basic salary.
	def __init__(self, name, basic_salary):
		self.name = name
		# Protected variable: intended for class/subclass usage.
		self._basic_salary = basic_salary

	def calculate_salary(self):
		# Base employee salary logic.
		return self._basic_salary


class Manager(Employee):
	# Manager inherits Employee and adds bonus.
	def __init__(self, name, basic_salary, bonus):
		super().__init__(name, basic_salary)
		self.bonus = bonus

	def calculate_salary(self):
		# Manager total salary = basic salary + bonus.
		return self._basic_salary + self.bonus


# ===================== 3) STUDENT INFORMATION SYSTEM (PUBLIC) =====================
class Student:
	# Public variables by default.
	def __init__(self, name, roll_no, marks):
		self.name = name
		self.roll_no = roll_no
		self.marks = marks

	def display_marks(self):
		# Method to display marks.
		print(f"Marks of {self.name} ({self.roll_no}): {self.marks}")


# ============== 4) ONLINE SHOPPING CART (PUBLIC + PROTECTED + PRIVATE) ==============
class ShoppingCart:
	def __init__(self, product_name, price):
		# Public member.
		self.product_name = product_name
		# Protected member.
		self._price = price

	def __apply_discount(self, discount_percent):
		# Private method for internal discount logic.
		# Example: 10% discount on 100 = 10
		discount_amount = (self._price * discount_percent) / 100
		return self._price - discount_amount

	def get_final_price(self, discount_percent):
		# Public method that calls private discount method.
		final_price = self.__apply_discount(discount_percent)
		return final_price


# ================= 5) HOSPITAL PATIENT RECORD SYSTEM (PRIVATE DATA) =================
class Patient:
	def __init__(self, name):
		self.name = name
		# Private list for confidential medical history.
		self.__medical_history = []

	def add_medical_record(self, record):
		# Authorized method to update private medical history.
		self.__medical_history.append(record)
		print("Medical record added successfully")

	def view_medical_history(self):
		# Authorized method to read private records.
		if len(self.__medical_history) == 0:
			print("No medical history available")
		else:
			print(f"Medical history of {self.name}:")
			for item in self.__medical_history:
				print("-", item)


# ============ 6) VEHICLE SPEED CONTROL SYSTEM (ENCAPSULATION + VALIDATION) ============
class Vehicle:
	def __init__(self):
		# Private speed variable.
		self.__speed = 0

	def set_speed(self, speed):
		# Validation: speed should be in valid range.
		# Here we allow 0 to 200 for demo.
		if 0 <= speed <= 200:
			self.__speed = speed
			print(f"Speed updated to {speed} km/h")
		else:
			print("Invalid speed! Enter value between 0 and 200")

	def get_speed(self):
		# Authorized method to read current speed.
		return self.__speed


# ============ 7) LIBRARY MANAGEMENT SYSTEM (PROTECTED FOR EXTENSIONS) ============
class Library:
	def __init__(self, initial_books=0):
		# Protected book count; intended for subclass use.
		self._book_count = initial_books

	def show_books(self):
		# Public method to view book count safely.
		print(f"Total books available: {self._book_count}")


class DigitalLibrary(Library):
	# Subclass can update protected book count.
	def add_books(self, count):
		if count > 0:
			self._book_count += count
			print(f"Added {count} books")
		else:
			print("Book count to add must be greater than 0")

	def remove_books(self, count):
		if count <= 0:
			print("Book count to remove must be greater than 0")
		elif count > self._book_count:
			print("Cannot remove more books than available")
		else:
			self._book_count -= count
			print(f"Removed {count} books")


# ================================ TEST SECTION ================================
if __name__ == "__main__":
	# 1) Bank Account Security System
	print("--- 1) Bank Account Security System ---")
	acc = BankAccount(1000)
	acc.deposit(500)
	acc.withdraw(300)
	print("Current Balance:", acc.get_balance())
	# Direct access like acc.__balance will fail due to private variable.
	print()

	# 2) Employee Payroll System
	print("--- 2) Employee Payroll System ---")
	emp = Employee("Ravi", 40000)
	mgr = Manager("Anita", 60000, 15000)
	print(f"Employee Salary ({emp.name}):", emp.calculate_salary())
	print(f"Manager Salary ({mgr.name}):", mgr.calculate_salary())
	print()

	# 3) Student Information System
	print("--- 3) Student Information System ---")
	stu = Student("Priya", "CS101", 88)
	print("Student Name:", stu.name)
	print("Student Roll No:", stu.roll_no)
	stu.display_marks()
	print()

	# 4) Online Shopping Cart System
	print("--- 4) Online Shopping Cart System ---")
	cart = ShoppingCart("Wireless Mouse", 1200)
	print("Product Name:", cart.product_name)
	print("Final Price after 10% discount:", cart.get_final_price(10))
	print()

	# 5) Hospital Patient Record System
	print("--- 5) Hospital Patient Record System ---")
	patient = Patient("Arjun")
	patient.add_medical_record("Fever - 2026")
	patient.add_medical_record("Allergy - Dust")
	patient.view_medical_history()
	print()

	# 6) Vehicle Speed Control System
	print("--- 6) Vehicle Speed Control System ---")
	car = Vehicle()
	car.set_speed(80)
	print("Current Speed:", car.get_speed())
	car.set_speed(250)  # invalid example
	print()

	# 7) Library Management System
	print("--- 7) Library Management System ---")
	dlib = DigitalLibrary(50)
	dlib.show_books()
	dlib.add_books(20)
	dlib.remove_books(10)
	dlib.show_books()
