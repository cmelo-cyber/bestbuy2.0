import pytest
from products import Product, LimitedProduct
from promotions import SecondHalfPrice,PercentDiscount,ThirdOneFree

def test_init_produkt_wird_erstellt():
    product = Product("Laptop", 999, 100)
    assert product.name == "Laptop"
    assert product.price == 999
    assert product.quantity == 100
    assert product.active == True

def test_init_product_ohne_namen():
    with pytest.raises(Exception) as e:
        product = Product("", 999, 100)

    assert str(e.value) =="Invalid input"
    assert e.type is Exception

def test_init_product_negativer_preis():
    with pytest.raises(Exception) as e:
        product = Product("Laptop", -999, 100)

    assert str(e.value) == "Invalid input"
    assert e.type is Exception

def test_produkt_leer():
    product = Product("Laptop", 999, 100)
    product.set_quantity(0)
    assert product.active == False

def test_produkt_kauf():
    product = Product("Laptop", 100, 10)
    total = product.buy(5)
    assert product.quantity == 5
    assert total == 500

def test_produkt_ausverkauft():
    product = Product("Laptop", 100, 2)

    with pytest.raises(ValueError, match=f"Nicht genügend Produkte verfügbar. Bestand: {product.quantity}"):
        total = product.buy(5)

def test_produkt_limitiert():
    limited_product = LimitedProduct("License", 100,100, 1)

    with pytest.raises(ValueError, match=f"Bestelllimit überschritten. Limit: {limited_product.limit}\n"):
        limited_product.buy(2)

def test_promotion_secondhalfprice():
    product = Product("MacBook Air M2", price=1000, quantity=100)
    second_half_price = SecondHalfPrice("Second Half price!")
    product.set_promotion(second_half_price)
    assert product.promotion == second_half_price
    assert product.promotion.name == "Second Half price!"
    total = product.buy(2)
    assert total == 1500


def test_promotion_thirdonefree():
    product = Product("MacBook Air M2", price=1000, quantity=100)
    third_one_free = ThirdOneFree("Third One Free!")
    product.set_promotion(third_one_free)
    assert product.promotion == third_one_free
    assert product.promotion.name == "Third One Free!"
    total = product.buy(3)
    assert total == 2000


def test_promotion_fiftypercent():
    product = Product("MacBook Air M2", price=1000, quantity=100)
    thirty_percent = PercentDiscount("50% off!", percent=50)
    product.set_promotion(thirty_percent)
    assert product.promotion == thirty_percent
    assert product.promotion.name == "50% off!"
    total = product.buy(1)
    assert total == 500