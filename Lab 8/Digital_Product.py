# Child class of Product (parent)

from Product import Product

class DigitalProduct(Product):     
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size
        
    def get_specific(self) -> float:    
        return self.__download_size 
    
    def get_types(self) -> str:
        return "Digital"
    
    def display_information(self) -> None:
        super().display_information()       # calls out Product display_information()
        print(f"Download Size: {self.get_specific()} MB, Type: {self.get_types()} ", end = "")
        self.get_supplier().display_information()
    
    def get_fulfilment_info(self) -> str:
        return "Product is delivered digitally."
        

