# Child class of Product (parent)

from Product import Product
from Can_Be_Shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):     
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight
    
    def get_types(self) -> str:
        return "Physical"
    
    def get_specific(self) -> float:
        return self.__weight
    
    def display_information(self) -> None:
        super().display_information()       # calls out Product display_information()
        print(f"Weight: {self.get_specific()} kg, Type: {self.get_types()} ", end = "")
        self.get_supplier().display_information()
    
    def calculate_shipping_cost(self) -> float:
        if self.__weight <= 0:
            return 0.0
            
        return self.get_specific() * 5.0
                    
    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping."
    
