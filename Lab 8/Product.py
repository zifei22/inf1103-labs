# Parent class of PhysicalProduct (child) & DigitalProduct (child)

from abc import ABC, abstractmethod
from Supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):
        self.__product_id = product_id     # stores product_id value into self.product_id (public)
        self.__name = name              
        self.price = price
        self.__stock = stock
        self.supplier: Supplier = supplier        
        
    def update_stock(self, quantity: int) -> None:
        self.__stock = quantity         #assigns new quantity to stock
        
    def get_product_id(self) -> str:
        return self.__product_id 
    
    def get_name(self) -> str:
        return self.__name
        
    def get_price(self) -> float:
        return self.price
    
    def get_stock(self) -> int:
        return self.__stock 
    
    def get_supplier(self) -> Supplier:
        return self.supplier
    
    def display_information(self) -> None:      # only displays current product (1 product)
        print(f"Product ID: {self.get_product_id()}, Name: {self.get_name()}", 
            f"Price: {self.get_price()}, Stock: {self.get_stock()},", end = " ")
    
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
    
    
        