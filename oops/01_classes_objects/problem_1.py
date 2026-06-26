
class Student:
    def __init__(self, name, age, marks):
        self.name  = name
        self.age   = age
        self.marks = marks

    def display_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nMarks: {self.marks}"
    
    def calculate_grade(self) -> str:
        if self.marks >= 90:
            return"A"
        elif self.marks >= 80:
            return"B"
        elif self.marks >= 70:
            return"C"
        elif self.marks >= 60:
            return"D"
        else:
            return"F"
    
    def get_grade(self):
        return f"Name: {self.name}\nGrade: {self.calculate_grade()}"
    
s1 = Student("Rahul",22,85)
s2 = Student("Amit",19,95)
s3 = Student("John",20,92)
s4 = Student("Joe",18,64)
s5 = Student("Rohit",20,59)

print(s2.display_info())
print(s2.get_grade())

students = [s1, s2, s3, s4, s5]
topper = max(students, key=lambda s:s.marks)
print(topper.name)
print(topper.marks)