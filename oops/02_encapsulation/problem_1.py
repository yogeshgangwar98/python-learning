
class BankAccount:
    def __init__(self, account_holder, balance = 500):
        self.account_holder = account_holder
        self.__balance      = balance

    def deposit(self, amount):
        if amount <= 0:
           raise ValueError("Deposit amount should be greater than zero.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount should be greater than zero.")
        if self.__balance < amount:
            raise ValueError("Insufficient balance")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
    

account = BankAccount("Rahul", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
print(vars(account)) # all the attributes are stores in the form of dict
print(dir(account)) # shows all the method of the class
#print(account.__balance) # Says no attribute find because balance is a private attribute and in vars(object) dict it stores as _BankAccount__balance
print(account._BankAccount__balance) # it fetches the balance