"""In this file the store class is defined"""

import products
from products import Product


class Store:
    def __init__(self, products_list):
        self.products_list = products_list


    def add_product(self, product):
        self.products_list.append(product)

    def remove_product(self, product):
        if product in self.products_list:
            self.products_list.remove(product)


    def get_total_quantity(self)->int:
        total = 0
        for product in self.products_list:
            total += product.get_quantity()
        return total


    def get_all_products(self):
        active_products = []
        for product in self.products_list:
            #print(product)
            if product.is_active() == True:
                active_products.append(product)
        #print(active_products)
        return active_products


    def order(self, shopping_list) -> float:
        cost = 0.0
        for product, quantity in shopping_list:
            cost += product.buy(quantity)
        return cost



# product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
#                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#                 products.Product("Google Pixel 7", price=500, quantity=250),
#                ]
#
# best_buy = Store(product_list)
# products = best_buy.get_all_products()
# print(best_buy.get_total_quantity())
# print(best_buy.order([(products[0], 1), (products[1], 2)]))