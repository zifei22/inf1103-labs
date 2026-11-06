import json
from Physical_Product import PhysicalProduct
from Digital_Product import DigitalProduct

from Inventory import Inventory
inventory_file = "inventory.json"


class File_Handling(Inventory):

    def load_inventory(self):
        inventory = Inventory()   
        try:
            with open(inventory_file, "r") as file:
                data = json.load(file)         
                #saves content of inventory_file into inventory
                for items in data:
                    if items.get("types") == "Physical":
                        product = PhysicalProduct(items['id'], items['name'], items['price'], 
                                                items['stock'], items['weight'])
                                                
                    elif items.get("types") == "Digital":
                        product = DigitalProduct(items['id'], items['name'], items['price'], 
                                                items['stock'], items['download_size'])

                    else:
                        continue
                    
                    inventory._productlist.append(product)
                status = "inventory.json found."   
                    
            
        except (FileNotFoundError, json.JSONDecodeError):     
            status = "inventory.json not found."
        
        return inventory, status        #inventory holds ALL the products in inventory.json


    def save_inventory(self, inventory):        # inventory here is referring to whole inventory list
        data = []
        for items in inventory._productlist:
            products_dict = {
                "id": items.get_product_id(),
                "name": items.get_name(),
                "price": items.get_price(), 
                "stock": items.get_stock()}
            
            if isinstance(items, PhysicalProduct):
                products_dict["types"] = "Physical"
                products_dict["weight"] = items.get_weight()    
                
            elif isinstance(items, DigitalProduct):
                products_dict["types"] = "Digital"
                products_dict["download_size"] = items.get_download_size()
                    
            data.append(products_dict)
            
        with open(inventory_file, "w") as file:
            json.dump(data, file)      #adding product to json file