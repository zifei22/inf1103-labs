from Product import Product
from Physical_Product import PhysicalProduct
from Digital_Product import DigitalProduct
from File_Handling import File_Handling


class Main:
    def __init__(self):
        self.__filehandle = File_Handling()
        # assigning the return values of load_inventory()
        self.__inventory, self.__status = self.__filehandle.load_inventory()    # self.__inventory refers to the whole list of inventory
        self.__running = False
        
    def run(self):

        if self.__status == "inventory.json found.":
            print("inventory.json found.\nInventory loaded successfully.")
        
        while not self.__running:
            print(f"----------- MENU -----------\n1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit")
            user_input = input("Enter option: ")
            
            if user_input == "1":
                self.__inventory.display_all() 
                
                
            elif user_input == "2":
                product_id = input("Add New Product\nProduct ID: ")
                result = self.__inventory.search_product(product_id)
                
                if result == None:
                    name = input("Product Name: ")
                    price = float(input("Price: "))
                    stock = float(input("Stock Quantity: "))                    
                    types = input("Is this a Physical or Digital Product? (P/D): ")
                    
                    if types.upper() == "P":
                        weight = float(input("Weight (in kg): "))
                        product = PhysicalProduct(product_id, name, price, stock, weight)
                        
                    elif types.upper() == "D":
                        download_size = float(input("Download Size (in MB): "))
                        product = DigitalProduct(product_id, name, price, stock, download_size)
                        
                    else:
                        print("Invalid product type. Product not added.")
                        continue
                                    
                    self.__inventory.add_product(product)
                    self.__filehandle.save_inventory(self.__inventory)           #saving the inventory so user able to update newly added stock
                    print("Product added successfully!")
                    
                else:
                    print("Product already exists!")    
                
                
            elif user_input == "3":
                product_id = input("Update Stock\nEnter Product ID: ")
                item = self.__inventory.search_product(product_id)
                
                if item != None:
                    print("Product Found:")
                    print(f"Name: {item.get_name()}\nCurrent Stock: {item.get_stock()}")
                    new_stock = input("New Stock Quantity: ")
                    Product.update_stock(item, new_stock)
                    print("Stock updated successfully!")
                    
                else:
                    print("No product found.")
            
            
            elif user_input == "4":
                product_id = input("Search Product\nEnter Product ID: ")
                item = self.__inventory.search_product(product_id)
                if item != None:
                    Product.display_information(item)
                else:
                    print("No product found.")

                
            
            elif user_input == "5":
                self.__filehandle.save_inventory(self.__inventory)
            
            else:
                print("Saving inventory before exit...\nInventory saved successfully")
                self.__filehandle.save_inventory(self.__inventory)
                print("Thank you for using Inventory Management System.\nProgram terminated.")
                self.__running = True


# __name__ (Program Entry Point)
if __name__=="__main__":
    main = Main()
    main.run()    


