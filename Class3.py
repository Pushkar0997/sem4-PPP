# Date - 13-02-2026

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    'Derivedclass Student inheriting from Person'
    def __init__(self,name,age,roll_no,marks):
        super().__init__(name,age)
        self.roll_no = roll_no
        self.marks = marks

        if roll_no < 0:
            raise ValueError("Roll number cannot be negative")
        
        if not (0 <= marks <= 100):
            raise ValueError("Marks must be between 0 and 100")

    def grade(self):
            if self.marks >= 90:
                return 'A'
            elif self.marks >= 80:
                return 'B'
            elif self.marks >= 70:
                return 'C'
            elif self.marks >= 60:
                return 'D'
            else:
                return 'F'
    
# Create an instance of Student
student = Student("Alice", 20, -1, 0)
student.display()  # Output: Name: Alice, Age: 20
print(f"Grade: {student.grade()}")  # Output: Grade: B