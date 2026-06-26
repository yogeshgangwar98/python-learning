from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Paid Rs{amount} using Credit Card")

class UPIProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Paid Rs{amount} using UPI")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Paid Rs{amount} using PayPal")

payments = [CreditCardProcessor(), UPIProcessor(), PayPalProcessor()]

for payment in payments:
    payment.process_payment(1000)