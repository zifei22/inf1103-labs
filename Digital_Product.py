# Child class of Product (parent)

from Product import Product

class DigitalProduct(Product):     
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock, download_size)
        self.__download_size = download_size
        
    def get_download_size(self) -> float:    
        return self.__download_size
    
    def get_types(self) -> str:
        return "Digital"
    
    def display_informations(self):
        super().display_information()
        print(f"Download Size: {self.__download_size} MB, Type: {self.get_types()}")
    
    def get_fulfilment_info(self) -> str:
        print(f"Product is delivered digitally.")    
        
    # def get_types(self) -> str:
    #     return "Digital" 
