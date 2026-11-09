from Product import Product
from OrderLine import OrderLine

class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []      # stores OrderLine as empty list

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, index: int) -> None:
        self.order_lines.pop(index)            
    
    def calculate_total(self) -> float:
        total = 0
        for lines in self.order_lines:
            total += lines.calculate_subtotal() 
            
        return total
        
    def get_order_lines(self) -> list[OrderLine]:
        return self.order_lines
    
    