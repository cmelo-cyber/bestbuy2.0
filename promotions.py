from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def apply_promotion(self, product, quantity)-> float:
        pass


class PercentDiscount(Promotion):
    def __init__(self,name, percent):
        super().__init__(name)
        self.percent = int(percent)/100

    def apply_promotion(self, product, quantity) -> float:
        total = float((float(product.price) * int(quantity))*(1-float(self.percent)))
        return total

class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        free_ones = int(int(quantity)/3)
        total = (int(quantity)-free_ones)*float(product.price)
        return total


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        half_ones=int(int(quantity)/2)
        total = float((int(quantity)-half_ones)*product.price) + float(half_ones*product.price*0.5)
        return total



second_half_price = SecondHalfPrice("Second Half price!")
# third_one_free = promotions.ThirdOneFree("Third One Free!")
# thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

#second_half_price.apply_promotion(product,amount)->