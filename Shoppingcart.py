class Operation:
    def add(self):
        pass
    def remove(self):
        pass

class Addtocart(Operation):
    def __init__(self, cart, product):
        self.cart = []
        self.product = product
    
    def add(self):
        self.cart.append(self.product)

    def remove(self):
        self.cart.remove(self.product)

#used command pattern here 
