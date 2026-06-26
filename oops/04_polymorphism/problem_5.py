class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary*(100/100)
    
class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary*(10/100)

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary*(20/100)

class Salesperson(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary*(15/100)
    
employees = [Developer("Rahul", 100000), Manager("Amit", 150000), Salesperson("Neha", 120000)]

for employee in employees:
    print(employee.calculate_bonus())
    

