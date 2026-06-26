
class Employee:
    def __init__(self, name, salary):
        self.name          = name
        self.__salary      = salary
        self.salary_change = [salary]

    def get_salary(self):
        return f"Name: {self.name} and Salary: {self.__salary}"

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        if salary > 5000000:
            raise ValueError("Salary cannot be greater than 50,00,000")
        self.__salary = salary
        self.salary_change.append(salary)

employee = Employee('Rahul',5000)
employee.set_salary(50000)
# employee.set_salary(-2000)
employee.set_salary(20000)
# employee.set_salary(20000000)
print(employee.salary_change)
print(employee.get_salary())