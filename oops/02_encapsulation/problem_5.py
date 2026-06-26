class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.__price = price

    @property
    def price(self):
        return {self.__price}
    
    @price.setter
    def price(self, price):
        if not 0 <= price <= 1000000:
            raise ValueError("Price should be between 0 and 10,00,000")
        self.__price = price

    def apply_discount(self, percent):
        if percent > 80:
            raise ValueError("Discount cannot exceed 80%")
        self.__price = (self.__price * (100-percent))/100
        print(f"Discount of {percent}% applied on Product {self.name}. New Price is now {self.__price}")

product = Product(1,"Laptop", 1000)
print(product.price)
product.price = 1500
print(product.price)
product.apply_discount(70)