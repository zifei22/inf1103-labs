class Inventory:
    def __init__(self):
        self._productlist = []      # creating an inventory list to hold all Product objects  
        
    def search_product(self, product_id):
        for items in self._productlist:
            if items.get_product_id() == product_id:
                return items
            
        return None
                
            
    def add_product(self, product):
        
        if self.search_product(product.get_product_id()) == None:
            self._productlist.append(product)
            
        else:
            print("Product already exists")
                
                
    def display_all(self):
        for items in self._productlist:
            items.display_informations()

        