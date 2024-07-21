from abc import ABC, abstractmethod


class Order:
    # Initialzing Order Items with status open
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    # Funtion responsible for adding item which take three parameters name quantity price
    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    # Calculating total price
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


# Creating a PaymentProcessor abstract class which can be extend by other payment processor
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(security_code, order: Order):
        pass

class CustomException(Exception):
    def __init__(self,exception):
        print(exception)

# class debit class which will extend PaymentProcessor
class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, security_code, order: Order):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
        raise


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, security_code, order: Order):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
        raise CustomException("Some thing wrong happen in Credit Processor")


class BitcoinPaymentProcessor(PaymentProcessor):
    def __init__(self, wallet_name) -> None:
        self.wallet_name = wallet_name

    def pay(self, security_code, order: Order):
        print("Processing bitcoin payment type")
        print(f"Verifying security code: {security_code}")
        print(f"Payment processed forn {self.wallet_name}")
        order.status = "paid"
        raise CustomException("Some thing wrong happen in Bitcoin Processor")


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
security_code = "2334432"
try:
    payment = CreditPaymentProcessor().pay(order=order, security_code=security_code)
except Exception as e:
    print("Some thing wrong")

# Initlizing extra thing with each processors
