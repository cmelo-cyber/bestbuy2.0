"""This is the main file for the program"""

import products
import store
from products import Limited_Product
from promotions import SecondHalfPrice,PercentDiscount,ThirdOneFree
# setup initial stock of inventory
# product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
#                  products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#                  products.Product("Google Pixel 7", price=500, quantity=250)
#                ]
#
# best_buy = store.Store(product_list)

# setup initial stock of inventory
# product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
#                  products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#                  products.Product("Google Pixel 7", price=500, quantity=250),
#                  products.No_Storage_Product("Windows License", price=125),
#                  products.Limited_Product("Shipping", price=10, quantity=250, limit=1)
#                ]

product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.No_Storage_Product("Windows License", price=125),
                 products.Limited_Product("Shipping", price=10, quantity=250, limit=1)
               ]

# Create promotion catalog
second_half_price = SecondHalfPrice("Second Half price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent = PercentDiscount("30% off!", percent=50)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[2].set_promotion(thirty_percent)

best_buy = store.Store(product_list)

#Define a Dictionary for the order function
prod_choices = {}
all_products = best_buy.get_all_products()
n = 1

for product in all_products:
    prod_choices[n] = product
    n += 1


def start(store):
    """This function displays the options to the user and makes the separation for the choices
    and calls the other functions"""
    choice = 0
    print("\n     Store Menu\n "
          "-----------\n"
          "1. List all products in store \n"
          "2. Show total amount in store \n"
          "3. Make an order \n"
          "4. Quit"
          )

    try:
        choice = int(input("Please choose a number: "))
    except ValueError:
        print("Error with your choice! Try again")
        return False

    if choice == 1:
        list_all_products()


    elif choice == 2:
        print(f"Total of {best_buy.get_total_quantity()} in the store")


    elif choice == 3:
        list_all_products()
        print("When you wand to finish order, enter empty text")
        orders = make_an_order()
        try:
            print(f"******\nOrder made! Total payment: ${best_buy.order(orders)}")
        except Exception as e:
            print(f"\n{e} you didnt order anything")

    elif choice == 4:
        return True

    elif choice <= 0 or choice > 4:
        print("Please enter a number from 1 to 4!")
        return False


def list_all_products():
    """This function prints all the products which are called by get_all_products() und numerates them"""
    print("-----------")
    products = best_buy.get_all_products()
    n = 1
    for product in products:
        print(f"{n}:", end="")
        product.show()
        n += 1
    print("-----------")


def make_an_order():
    """This function takes the order and returns the order list"""
    ordering = True
    order_list = []
    while ordering:

        order_number = input("Which product do you want ?")
        amount = input("How many do you want?")


        if order_number =="" and amount =="":       # Check if the user want to return to Store
            return order_list

        if order_number=="" or amount =="":
            print("Please fill both fields")
            continue

        if  isinstance(prod_choices[int(order_number)], Limited_Product)  and int(amount) > prod_choices[int(order_number)].limit:
            # soll checken, ob die bestellung einen limit besitzt und den menge mit dem limit vergleichen
            print("Bestell-Limit überschritten")
            continue

        try:
            amount = int(amount)
            if amount <= 0:
                print("Amount must be greater than 0")
                continue
        except ValueError:
            print("Please enter a valid quantity")
            continue
        #print(prod_choices)
        #prod_choices is a dict defined at the beginning
        try:
            product = prod_choices[int(order_number)]
        except (ValueError, KeyError):
            print("Invalid product number.")
            continue
        order_list.append((product,amount))
        print("Product added to list!")
        #for order in order_list:
        #    print(f"{order[0].name}, Price: {order[0].price} and {amount}")


def main():
    """This function calls the start function and has the while loop"""
    stop = False
    while not stop:
        stop = start(best_buy)


if __name__=="__main__":
    main()

