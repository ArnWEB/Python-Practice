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

    # Calculating payment mechanism
    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


# As Single Responsibilty says that we every class should have single responsibilty so Seggreating pay method to another Class


class PaymentProcessor:
    #initlizing constuctore for inilizing security_code,order
    def __init__(self, security_code,order:Order) -> None:
        self.security_code = security_code
        self.order=order
    #credit payment for order
    def credit_pay(self):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        self.order = "paid"
    #debit payment for order
    def debit_pay(self):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        self.order = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
security_code="2334432"
payment=PaymentProcessor(security_code=security_code,order=order)
payment.debit_pay()
