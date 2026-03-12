# ======================== PYTHON INHERITANCE - THEORY ========================
#
# What is Inheritance?
# Inheritance is an OOP feature where one class (child/subclass) uses properties
# and methods of another class (parent/base class).
#
# Why use inheritance?
# 1. Code reuse: write common code once in base class.
# 2. Easy extension: child class can add new features.
# 3. Better structure: related classes are organized clearly.
#
# Common terms:
# - Parent/Base class: class whose members are inherited.
# - Child/Derived class: class that inherits from parent class.
#
# Types covered in this file:
# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Multiple Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance
#
# ============================================================================


# ======================== 1) SINGLE INHERITANCE ========================
# Problem context: Online learning platform

class Course:
	# Base class with common course details.
	def __init__(self, title, duration):
		# Store course title in object variable.
		self.title = title
		# Store course duration (example: "8 weeks").
		self.duration = duration

	def show_course_details(self):
		# Print common details available for all courses.
		print(f"Course Title: {self.title}")
		print(f"Duration: {self.duration}")


class ProgrammingCourse(Course):
	# Child class inherits all members of Course.
	def __init__(self, title, duration, language):
		# Call parent class constructor to set common fields.
		super().__init__(title, duration)
		# Add child-specific field.
		self.language = language

	def show_programming_details(self):
		# Reuse parent class method for common details.
		self.show_course_details()
		# Print extra feature specific to ProgrammingCourse.
		print(f"Programming Language: {self.language}")


# ======================== 2) MULTILEVEL INHERITANCE ========================
# Problem context: Banking system

class Account:
	# Level 1: Base class
	def __init__(self, holder_name, balance):
		self.holder_name = holder_name
		self.balance = balance

	def open_account(self):
		# Basic operation defined in top-level class.
		print(f"Account opened for {self.holder_name} with balance {self.balance}")


class SavingsAccount(Account):
	# Level 2: Inherits from Account
	def calculate_interest(self, rate):
		# Simple interest calculation for savings account.
		interest = self.balance * rate / 100
		print(f"Savings Interest at {rate}%: {interest}")
		return interest


class PremiumSavingsAccount(SavingsAccount):
	# Level 3: Inherits from SavingsAccount
	def premium_benefit(self, premium_rate):
		# Premium account gets higher interest rate.
		premium_interest = self.balance * premium_rate / 100
		print(f"Premium Interest at {premium_rate}%: {premium_interest}")
		return premium_interest


# ======================== 3) MULTIPLE INHERITANCE ========================
# Problem context: Smart home system

class VoiceControl:
	# Parent class 1
	def enable_voice_control(self):
		print("Voice control enabled.")


class RemoteControl:
	# Parent class 2
	def enable_remote_control(self):
		print("Remote control enabled.")


class SmartLight(VoiceControl, RemoteControl):
	# Child class inherits from both VoiceControl and RemoteControl.
	def turn_on_light(self):
		print("Smart light turned ON.")


# ======================== 4) HIERARCHICAL INHERITANCE ========================
# Problem context: University examination system

class User:
	# Base class common for both Student and Faculty.
	def __init__(self, name, user_id):
		self.name = name
		self.user_id = user_id

	def show_user_info(self):
		print(f"Name: {self.name}, ID: {self.user_id}")


class Student(User):
	# Child class 1 inheriting from User.
	def submit_exam(self):
		print(f"Student {self.name} submitted exam.")


class Faculty(User):
	# Child class 2 inheriting from User.
	def evaluate_exam(self):
		print(f"Faculty {self.name} evaluated exam papers.")


# ======================== 5) HYBRID INHERITANCE ========================
# Problem context: Hospital management system
# Hybrid = combination of hierarchical + multiple inheritance.

class Person:
	# Top base class.
	def __init__(self, name):
		self.name = name

	def show_person(self):
		print(f"Person Name: {self.name}")


class Doctor(Person):
	# Derived from Person (hierarchical branch 1).
	def diagnose(self):
		print(f"Dr. {self.name} is diagnosing a patient.")


class Nurse(Person):
	# Derived from Person (hierarchical branch 2).
	def assist(self):
		print(f"Nurse {self.name} is assisting in treatment.")


class SpecializedRole:
	# Separate class to represent specialized medical capability.
	def perform_special_surgery(self):
		print("Performing specialized surgery.")


class Surgeon(Doctor, SpecializedRole):
	# Multiple inheritance:
	# - gets person/doctor behavior from Doctor
	# - gets specialization behavior from SpecializedRole
	def operate(self):
		print(f"Surgeon {self.name} is operating.")


# ======================== TEST / DEMO SECTION ========================
# This section maps directly to your exam-style one-line statements.

if __name__ == "__main__":
	# 1) Single inheritance in online education system.
	print("--- 1) Single Inheritance: Online Education ---")
	python_course = ProgrammingCourse("Python Basics", "8 weeks", "Python")
	python_course.show_programming_details()
	print()

	# 2) Multilevel inheritance in banking application.
	print("--- 2) Multilevel Inheritance: Banking ---")
	premium_acc = PremiumSavingsAccount("Pushkar", 50000)
	premium_acc.open_account()
	premium_acc.calculate_interest(5)
	premium_acc.premium_benefit(8)
	print()

	# 3) Multiple inheritance in smart device system.
	print("--- 3) Multiple Inheritance: Smart Device ---")
	home_light = SmartLight()
	home_light.enable_voice_control()
	home_light.enable_remote_control()
	home_light.turn_on_light()
	print()

	# 4) Hierarchical inheritance in university system.
	print("--- 4) Hierarchical Inheritance: University ---")
	student_user = Student("Aman", "ST101")
	faculty_user = Faculty("Dr. Mehta", "FC202")
	student_user.show_user_info()
	student_user.submit_exam()
	faculty_user.show_user_info()
	faculty_user.evaluate_exam()
	print()

	# 5) Hybrid inheritance in hospital system.
	print("--- 5) Hybrid Inheritance: Hospital ---")
	surgeon_user = Surgeon("Rao")
	surgeon_user.show_person()
	surgeon_user.diagnose()
	surgeon_user.perform_special_surgery()
	surgeon_user.operate()
