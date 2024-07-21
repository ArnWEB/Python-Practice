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
    def pay(order: Order):
        pass


class Auth(ABC):
    @abstractmethod
    def is_verified(self)->bool:
        pass

class AuthSMSProcesssor(Auth):
    def __init__(self) -> None:
        self.verified = False
        self.security_code = None

    def auth_sms(self, code):
        print("Auth SMS is verified for Payment Processor")
        self.security_code = code
        self.verified = True

    def is_verified(self)->bool:
        return self.verified


# Now I have to add auth_sms method in every class which is not good practice


class CustomException(Exception):
    def __init__(self, exception):
        print(exception)


# class debit class which will extend PaymentProcessor
class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, sms_auth: Auth) -> None:
        self.auth_sms = sms_auth

    def pay(self, order: Order):
        if not self.auth_sms.verified():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.auth_sms.security_code}")
        order.status = "paid"
        raise


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, sms_auth: Auth) -> None:
        self.auth_sms = sms_auth

    def pay(self, order: Order):
        print(self.auth_sms.verified)
        if not self.auth_sms.verified:
            raise Exception("Not authorized")
        print("Processing credit payment type")
        print(f"Verifying security code: {self.auth_sms.security_code}")
        order.status = "paid"


class BitcoinPaymentProcessor(PaymentProcessor):
    def __init__(self, wallet_name, email) -> None:
        self.wallet_name = wallet_name
        self.email = email

    def pay(self, order: Order):
        print("Processing bitcoin payment type")
        print(f"Verifying email address: {self.email}")
        print(f"Payment processed forn {self.wallet_name}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
security_code = "2334432"

auth=AuthSMSProcesssor()
auth.auth_sms(security_code)
try:
    payment = CreditPaymentProcessor(auth)
    payment.pay(order=order)
except Exception as e:
    print(e)

# Here I have added auth_sms method in every class which is not good practice so that is where Interface segeratrion is necessary
