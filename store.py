class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.orders = []

class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.items = {}
        self.total = 0.0
    
    def add_item(self, product, quantity):
        if product.update_stock(quantity):
            if product.id in self.items:
                self.items[product.id][1] += quantity
            else:
                self.items[product.id] = [product, quantity]
            self.total += product.price * quantity
            return True
        return False
    
    def checkout(self):
        order = {"items": self.items.copy(), "total": self.total}
        self.customer.orders.append(order)
        self.items = {}
        self.total = 0.0
        return order

# Demo
products = [
    Product(1, "Laptop", 1000, 5),
    Product(2, "Mouse", 25, 20),
    Product(3, "Keyboard", 50, 15)
]

customer = Customer(1, "John Doe")
cart = ShoppingCart(customer)

cart.add_item(products[0], 1)
cart.add_item(products[1], 2)
print(f"Cart total: ${cart.total}")

order = cart.checkout()
print(f"Order completed with total: ${order['total']}")