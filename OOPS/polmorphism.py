# Example of Polymorphism in Python

class Payment:
    def pay(self, amount):
        print("Payment processing for the amount:", amount)


class CreditCardPayment(Payment):
    def pay(self, amount):
        print("CREDIT CARD PAYMENT:", amount)

class UPI(Payment):
    def pay(self, amount):
        print("UPI PAYMENT:", amount)   

class CashPayment(Payment):
    def pay(self, amount):
        print("CASH PAYMENT:", amount)

payments = [CreditCardPayment(), UPI(), CashPayment()]

for payment in payments:
    payment.pay(100)  # Each payment method processes the payment differently

