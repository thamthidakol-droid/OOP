#Practice 6: Product Management System

class Product:
    store_name = "ITC Online store"
    product_count = 0
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.product_count += 1
    def display_product(self):
        print("Name:", self.name)
        print("Price: $", self.price)
        print("Quantity:", self.quantity)
        print("Total Value: $", self.total_value())
        print("------------------------")
    def total_value(self):
        return self.price * self.quantity
    @classmethod
    def get_product_count(cls):
        return cls.product_count
    @staticmethod
    def is_valid_price(price):
        return price > 0

product1 = Product("Laptop", 800, 5)
product2 = Product("Mouse", 20, 10)
product3 = Product("Keyboard", 50, 8)
print("==========", Product.store_name, "==========")
product1.display_product()
product2.display_product()
product3.display_product()
total_inventory = (
    product1.total_value() + product2.total_value() + product3.total_value()
)
print("Total Inventory Value: $", total_inventory)
print("Total Products:", Product.get_product_count())
print("Is $70 a valid price?", Product.is_valid_price(70))
print("Is $-100 a valid price?", Product.is_valid_price(-100))

