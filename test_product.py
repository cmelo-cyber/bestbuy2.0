import pytest
from products import Product

def test_init_Produkt_wird_erstellt():
    product = Product("Laptop", 999, 100)
    assert product.name == "Laptop"
    assert product.price == 999
    assert product.quantity == 100
    assert product.active == True

def test_init_Product_ohne_Namen():
    with pytest.raises(Exception) as e:
        product = Product("", 999, 100)

    assert str(e.value) =="Invalid input"
    assert e.type is Exception

def test_init_Product_negativer_Preis():
    with pytest.raises(Exception) as e:
        product = Product("Laptop", -999, 100)

    assert str(e.value) == "Invalid input"
    assert e.type is Exception

def test_Produkt_leer():
    product = Product("Laptop", 999, 100)
    product.set_quantity(0)
    assert product.active == False

def test_Produkt_kauf():
    product = Product("Laptop", 100, 10)
    total = product.buy(5)
    assert product.quantity == 5
    assert total == 500

def test_Produkt_ausverkauft():
    product = Product("Laptop", 100, 2)

    with pytest.raises(ValueError, match=f"Nicht genügend Produkte verfügbar. Bestand: {product.quantity}"):
        total = product.buy(5)

