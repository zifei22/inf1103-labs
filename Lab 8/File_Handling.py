import json
import os
from Physical_Product import PhysicalProduct
from Digital_Product import DigitalProduct
from Inventory import Inventory
from Supplier import Supplier
inventory_file = r"C:\Users\wongz\OneDrive - Singapore Institute Of Technology\Y1T1\INF 1103 - Program w DevOps\weekly labs\Lab 8\inventory.json"


class File_Handling():

    def load_inventory(self) -> tuple[Inventory, str]:
        inventory = Inventory()   
        try:
            with open(inventory_file, "r") as file:
                data = json.load(file)         
                #saves content of inventory_file into inventory
                for items in data:
                    supplier_data = items['supplier']
                    supplier = Supplier(supplier_data['supplier id'], supplier_data['supplier name'], supplier_data['supplier contact email'])
                    
                    if items.get("types") == "Physical":
                        product = PhysicalProduct(items['id'], items['name'], items['price'], 
                                                items['stock'], items['weight'], supplier)
                                                
                    elif items.get("types") == "Digital":
                        product = DigitalProduct(items['id'], items['name'], items['price'], 
                                                items['stock'], items['download size'], supplier)

                    else:
                        continue
                    
                    inventory.add_product(product)
                status = "inventory.json found."   
                    
            
        except (FileNotFoundError, json.JSONDecodeError):     
            status = "inventory.json not found."
        
        return inventory, status        #inventory holds ALL the products in inventory.json


    def save_inventory(self, inventory: Inventory) -> None:        # inventory here is referring to whole inventory list
        data = []
        for items in inventory.get_products_list():
            supplier = items.get_supplier()
            
            if items.get_types() == "Physical":
                specific_key = "weight"
                
            else:
                specific_key = "download size"
            
            products_dict = {
                "id": items.get_product_id(),
                "name": items.get_name(),
                "price": items.get_price(), 
                "stock": items.get_stock(),
                "types": items.get_types(),
                specific_key: items.get_specific(),
                "supplier": {"supplier id": supplier.get_supplier_id(),
                            "supplier name": supplier.get_supplier_name(),
                            "supplier contact email": supplier.get_contact_email()}}
            data.append(products_dict)
        with open(inventory_file, "w") as file:
            json.dump(data, file)      #adding product to json file


            