# Child class of Product (parent)

from Product import Product
from Can_Be_Shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):     
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock, weight)
    
    def get_types(self) -> str:
        return "Physical"
    
    def display_informations(self):
        super().display_information()
        print(f"Weight: {self.get_weight()} kg, Type: {self.get_types()}")
    
    def calculate_shipping_cost(self) -> float:
        if self.__weight <= 0:
            shipping_cost = 0.0
            
        else:
            shipping_cost = self.get_weight() * 5.0
            
        return f"Shipping cost for {self.get_name()} (Weight: {self.get_weight()}kg) is ${shipping_cost}"
        
    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping."
        
    # def get_types(self) -> str:
    #     return "Physical" 
