
class Employee:
    total_employees = 0
    def __init__(self, name, salary, department):
        self.name       = name
        self.salary     = salary
        self.department = department
        Employee.total_employees += 1

    def display_employee(self):
        print(f"Name: {self.name}\nSalary: {self.salary}\nDepartment: {self.department}")

    def display_total_employees(self):
        print(f"Total Employees = {Employee.total_employees}")

e1 = Employee("Rahul",23000,"Accounts")
e2 = Employee("Amit",46000,"Management")
e3 = Employee("Neha",35000,"Development")

e1.display_employee()
e2.display_employee()
e3.display_employee()

e3.display_total_employees()