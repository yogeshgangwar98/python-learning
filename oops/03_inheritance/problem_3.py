class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
        
    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nRoll no.: {self.roll_number}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSubject: {self.subject}")

student = Student("Rahul",22,101)

student.display_info()