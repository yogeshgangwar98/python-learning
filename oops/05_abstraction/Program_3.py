from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def job_role(self):
        pass

class Developer(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.slary = salary

    def job_role(self):
        return "Developer"
    
    def calculate_salary(self):
        return self.slary

class Manager(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.slary = salary 

    def job_role(self):
        return "Manager"
    
    def calculate_salary(self):
        return self.slary    


dev = Developer(
    "Rahul",
    50000
)

print(dev.job_role())
print(dev.calculate_salary())