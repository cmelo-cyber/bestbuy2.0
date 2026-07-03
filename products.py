"""In this file the product class is defined"""

class Product:

    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise Exception("Invalid input")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True




    def get_quantity(self)-> int:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self)->bool:
        return self.active

    def active(self):
        self.active = True

    def deactive(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity)->float:
        if self.quantity < quantity:
            raise ValueError(
                f"Nicht genügend Produkte verfügbar. Bestand: {self.quantity}"
            )
        else:
            self.quantity -= quantity
        return self.price * quantity



# bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
# mac = Product("MacBook Air M2", price=1450, quantity=100)
#
# print(bose.buy(50))
# print(mac.buy(100))
# print(mac.is_active())
#
# bose.show()
# mac.show()
#
# bose.set_quantity(1000)
# bose.show()

