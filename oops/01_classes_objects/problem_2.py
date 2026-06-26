
class BankAccount:
    def __init__(self,account_holder, balance = 500):
        self.account_holder = account_holder
        self.balance        = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive"
        self.balance += amount
        return f"{amount} is deposited successfully, your current balance is {self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive"
        if amount > self.balance:
            res = "Insufficient balance"
        else:
            self.balance -= amount
            res = f"{amount} is withdrawn successfully, your current balance is {self.balance}"
        return res

    def show_balance(self):
        return f"Hi {self.account_holder}, your current balance is {self.balance}."
    
ac1 = BankAccount("Rahul")
ac2 = BankAccount("Amit",1000)

print(ac2.show_balance())
print(ac2.deposit(1200))
print(ac2.withdraw(400))
print(ac2.show_balance())