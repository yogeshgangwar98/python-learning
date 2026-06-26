class Product:
    def __init__(self, id, name, price):
        self.id     = id
        self.name   = name
        self.price  = price
    
    def show_product(self):
        print(f"ID: {self.id}\nName: {self.name}\nPrice: {self.price}")

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Product added Successfully")

    def remove_product(self,id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                print(f"Removed product with ID: {id}")
                return
        print("No product found with given ID")

    def show_cart(self):
        for product in self.products:
            product.show_product()

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        print(total)

cart = Cart()

 # Add Product
cart.add_product(Product(1, "Keyboard",499))
cart.add_product(Product(2, "Laptop", 799))
cart.add_product(Product(3, "Mouse", 649))
# Display all
cart.show_cart()
cart.total_price()

# Remove
cart.remove_product(2)
cart.remove_product(2)
cart.show_cart()