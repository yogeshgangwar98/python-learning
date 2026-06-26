class Payment:
    def pay(self, amount):
        print(f"Paid Rs{amount} using General Payment")

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs{amount} using Credit Card")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs{amount} using UPI")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs{amount} using PayPal")

payments = [CreditCardPayment(), UPIPayment(), PayPalPayment()]

for payment in payments:
    payment.pay(1000)
