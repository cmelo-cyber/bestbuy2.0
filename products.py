"""In this file the product class is defined"""
from promotions import Promotion


class Product:
    """Diese Klasse stellt einzelne Produkte dar.
    Sie hat folgende Attribute (Name, Price, Quantity, Active, Promotion: class)und Methoden wie show und buy"""
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise Exception("Invalid input")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None # This attribute is the object
        # of subclass promotion (one of three half,percent,third...)

    def get_quantity(self)-> int:
        """returns quantity"""
        return self.quantity

    def set_quantity(self, quantity):
        """sets quantity"""
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def get_promotion(self)-> int:
        """returns promo"""
        return self.promotion

    def set_promotion(self, promotion):
        """sets promo"""
        self.promotion = promotion
        if self.promotion == "":
            self.promotion = None

    def is_active(self)->bool:
        """returns activity"""
        return self.active

    def active(self):
        """sets activ"""
        self.active = True

    def deactive(self):
        """sets deactiv"""
        self.active = False

    def show(self):
        """Shows the product information"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion:{self.promotion.name}")

    def buy(self, quantity)->float:
        """Takes the amount of pieces and calculates the total.
        It also reduces the amount in the stock and checks if there is a promotion"""
        if self.quantity < quantity:
            raise ValueError(
                f"Nicht genügend Produkte verfügbar. Bestand: {self.quantity}"
            )
        else:
            if self.promotion:
                total = self.promotion.apply_promotion(self, quantity) # self here is the product object which is handed to apply_promo
            else:
                self.quantity -= quantity
                total = self.price * quantity
        # if there is promotion  if no return self.price * quantity
        #otherwise if promotion is activ: call applypromotion
        return total



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
class NoStorageProduct(Product):
    """This class is for products with are not stored like licenses. It inherits from product class"""
    def __init__(self, name, price, ):
        super().__init__(name, price, 0)

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity is 0 for this Product")

    def buy(self, quantity)->float:
        return self.price * quantity


class LimitedProduct(Product):
    """This class is for products which are limited. It inherits from product class"""
    def __init__(self, name, price, quantity, limit):
        super().__init__(name, price, quantity)
        self.limit = limit

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity is limited to: {self.limit}")

    def buy(self, quantity)->float:
        if self.quantity < quantity:
            raise ValueError(
                f"Nicht genügend Produkte verfügbar. Bestand: {self.quantity}"
            )

        if self.limit < quantity:
            raise ValueError(
                f"Bestelllimit überschritten. Limit: {self.limit}\n"
            )


        self.quantity -= quantity
        return self.price * quantity
