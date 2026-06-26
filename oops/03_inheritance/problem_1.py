class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}\nSalary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def display_info(self):
        print(f"Name: {self.name}\nSalary: {self.salary}\nLanguage: {self.programming_language}")
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display_info(self):
        print(f"Name: {self.name}\nSalary: {self.salary}\nTeam Size: {self.team_size}")

developer = Developer("Rahul", 80000, "Python")
manager = Manager("Amit", 120000, 10)

developer.display_info()
manager.display_info()