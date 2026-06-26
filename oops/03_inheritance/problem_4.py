class Account:
    def __init__(self, account_number, balance):
        self. account_number = account_number
        self.balance         = balance

    def deposit(self, amount):
        if amount <=0 :
            raise ValueError("Deposit a positive amount")
        self.balance += amount
        print(f"{amount} deposited successfully.\nCurrent balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        if not (0 <= interest_rate <= 100):
            raise ValueError("Interest rate must be between 0 and 100")
        self.interest_rate = interest_rate

    def calculate_interest(self):
        calculated_interest = (self.balance * self.interest_rate)/100
        print(f"Interest Earned: {calculated_interest}")

class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, reward_points):
        super().__init__(account_number, balance, interest_rate)
        self.reward_points = reward_points

    def add_reward_points(self, reward):
        if reward <=0 :
            raise ValueError("Reward point should be positive")
        self.reward_points += reward
        print(f"{reward} reward points added.\nTotal reward points: {self.reward_points}")

premium = PremiumSavingsAccount(101,10000,5,100)
premium.deposit(5000)
premium.calculate_interest()
premium.add_reward_points(50)