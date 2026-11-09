from Product import Product

class Inventory:
    def __init__(self):
        self.products: list[Product] = []      # creating an inventory list to hold all Product objects  
    
    def get_products_list(self) -> list[Product]:
        return self.products
        
    def search_product(self, product_id) -> Product | None:
        for items in self.products:
            if items.get_product_id() == product_id:
                return items
            
        return None
                
            
    def add_product(self, product: Product) -> None:
        
        if self.search_product(product.get_product_id()) == None:
            self.products.append(product)
            
        else:
            print("Product already exists")
                
    
    def remove_product(self, product_id: str) -> None:
        
        product = self.search_product(product_id)
        if product != None:
            self.products.remove(product)
            print(f"Product {product_id} removed")
            
        else:
            print("Product does not exists")
        
                
    def display_all(self) -> None:
        for items in self.products:
            items.display_information()

        