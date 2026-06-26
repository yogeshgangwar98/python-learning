class Student:
    def __init__(self, name, marks):
        self.name    = name
        self.__marks = marks
    
    @property
    def marks(self):
        return self.__marks
    
    @marks.setter
    def marks(self, marks):
        if not 0 <= marks <= 100:
            raise ValueError("Marks should be between 0 and 100")
        self.__marks = marks

student = Student("Rahul", 80)

print(student.marks)
student.marks = 100
print(student.marks)