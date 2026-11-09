from Product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity = quantity
    
    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity
    
    def get_product(self) -> Product:
        return self.product
    
    def get_quantity(self) -> int:
        return self.quantity