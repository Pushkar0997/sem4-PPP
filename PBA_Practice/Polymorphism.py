# ======================== PYTHON POLYMORPHISM - THEORY ========================
#
# What is Polymorphism?
# Polymorphism means "many forms".
# In Python, different objects can be used in the same way if they provide
# the same method name.
#
# Example in this file:
# - Teacher object has speak()
# - Student object has speak()
# - Instructor object has speak()
# - Learner object has speak()
# etc.
#
# A single function can call obj.speak() for all of them.
# This is called run-time polymorphism (method decided at run time).
#
# Duck Typing in Python:
# "If it looks like a duck and quacks like a duck, treat it like a duck."
# Meaning: Python does not require inheritance to support polymorphism.
# If object has required method (like speak), it will work.
#
# Benefits:
# 1. Flexible and scalable design.
# 2. Easy to add new roles/classes.
# 3. Common function does not need modification for new role.
#
# ============================================================================


# ==================== Common Polymorphic Function ====================
def perform_speaking_action(person_object):
	# This function accepts ANY object.
	# It only assumes that object has a speak() method.
	person_object.speak()


# ==================== Problem 1: Smart Classroom ====================
class Teacher:
	# Teacher class with role-specific speak behavior.
	def speak(self):
		print("Teacher: Today we will learn about polymorphism.")


class Student:
	# Student class with different speak behavior.
	def speak(self):
		print("Student: Sir, can you explain it once more?")


# ==================== Problem 2: Online Learning Platform ====================
# No inheritance is used here.
# This demonstrates dynamic behavior through duck typing.

class Instructor:
	# Instructor explains concepts.
	def speak(self):
		print("Instructor: Let me explain the concept with an example.")


class Learner:
	# Learner asks doubts.
	def speak(self):
		print("Learner: I have a doubt in this topic.")


# ==================== Problem 3: School Role Management System ====================
class Principal:
	# Principal role speaking behavior.
	def speak(self):
		print("Principal: Maintain discipline and focus on learning.")


class Librarian:
	# Librarian role speaking behavior.
	def speak(self):
		print("Librarian: Please return borrowed books on time.")


# New role added without changing perform_speaking_action function.
class Counselor:
	# Added to show scalability.
	def speak(self):
		print("Counselor: Feel free to discuss your academic concerns.")


# ==================== Problem 4: Corporate Training Module ====================
class Trainer:
	# Trainer conducts session.
	def speak(self):
		print("Trainer: Welcome everyone, let's begin today's session.")


class Employee:
	# Employee participates in training.
	def speak(self):
		print("Employee: I am actively participating in the training.")


class HR:
	# HR monitors and supports the session.
	def speak(self):
		print("HR: Attendance and feedback are being monitored.")


# ==================== Test / Demo Section ====================
if __name__ == "__main__":
	# ---------- Problem 1 Demo ----------
	print("--- Problem 1: Smart Classroom Communication System ---")
	school_teacher = Teacher()
	school_student = Student()
	perform_speaking_action(school_teacher)
	perform_speaking_action(school_student)
	print()

	# ---------- Problem 2 Demo ----------
	print("--- Problem 2: Online Learning Platform (No Inheritance) ---")
	session_instructor = Instructor()
	session_learner = Learner()
	perform_speaking_action(session_instructor)
	perform_speaking_action(session_learner)
	print()

	# ---------- Problem 3 Demo ----------
	print("--- Problem 3: School Role Management System ---")
	role_teacher = Teacher()
	role_student = Student()
	role_principal = Principal()
	role_librarian = Librarian()
	role_counselor = Counselor()  # newly added role

	# Same common function handles all roles.
	perform_speaking_action(role_teacher)
	perform_speaking_action(role_student)
	perform_speaking_action(role_principal)
	perform_speaking_action(role_librarian)
	perform_speaking_action(role_counselor)
	print()

	# ---------- Problem 4 Demo ----------
	print("--- Problem 4: Corporate Training Module ---")
	corp_trainer = Trainer()
	corp_employee = Employee()
	corp_hr = HR()

	# One function, multiple object behaviors at run time.
	perform_speaking_action(corp_trainer)
	perform_speaking_action(corp_employee)
	perform_speaking_action(corp_hr)

	print()
	print("Run-time polymorphism demonstrated successfully.")
