# Parent class of PhysicalProduct (child) & DigitalProduct (child)

from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, stock, weight):
        self.__product_id = product_id     # stores product_id value into self.product_id (public)
        self.__name = name              
        self.__price = price
        self.__stock = stock
        self.__weight = weight
        
    def update_stock(self, quantity):
        self.__stock = quantity         #assigns new quantity to stock

    def display_information(self):      # only displays current product (1 product)
        print(f"Product ID: {self.__product_id}, Name: {self.__name}, Price: {float(self.__price)}, Stock: {int(self.__stock)}", end = " ")
        
    def get_product_id(self):
        return self.__product_id 
    
    def get_name(self) -> str:
        return self.__name
        
    def get_price(self) -> float:
        return self.__price
    
    def get_stock(self) -> int:
        return self.__stock 
    
    def get_weight(self) -> float:
        return self.__weight
    
    @abstractmethod
    def get_fulfilment_info(self):
        pass
        