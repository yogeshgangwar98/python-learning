class InsufficientBalanceError(Exception):
    pass

balance = 1000

def withdraw(amount):
    try:
        global balance
        if balance < amount:
            raise InsufficientBalanceError("Insufficient Balanace")
        balance -= amount
    except InsufficientBalanceError as isbe:
        return f"Error: {isbe}"
    else:
        return f"New balance left: {balance}"

print(withdraw(100))