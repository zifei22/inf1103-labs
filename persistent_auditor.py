max_capacity = 500
tax_rate = 0.1    #10% tax rate
inventory_file = "inventory.txt"


def get_valid_input():
    quantity = 0
    rejected_entries = 0
 
    while True: 
        user_input = input("Enter stock quantity or 'quit' to exit: ") 
   
        if user_input.isdigit() == False: #check for letters/negative numbers
       
            if user_input.lower() == "quit":
                return "quit", rejected_entries          
     
            if user_input.startswith("-"):                  #to account for negative numnbers
                print("Invalid input. Please enter a non-negative stock quantity.")
                rejected_entries += 1
                continue
     
            if str(user_input).count(".") == 1:             #to account for the decimals
                if float(user_input).is_integer():          #if input is a valid decimal
                    quantity += int(float(user_input))
                    return quantity, rejected_entries            

                else:
                    print("Invalid input. Please enter a whole number.")
                    rejected_entries += 1
                    continue
     
            else:
                print("Invalid input. Please enter a valid stock quantity or 'quit' to exit.")
                rejected_entries += 1
                continue
   
        else:
            user_input = int(user_input)
            if user_input == 0:           #check for 'integer' input
                print("No items added to inventory. Please enter a valid stock quantity or 'quit' to exit.")    
                rejected_entries += 1
                continue
                     
            else:
                quantity += user_input
                # continue
                return quantity, rejected_entries                
                              
       
def process_delivery(current_total, new_value):     #account for exceed value, return total,
    new_total = new_value + current_total 

    if new_total > max_capacity:
        print("Overstock alert! You cannot add 500 items. Maximum capacity is 500.")
        return None
  
    else:
        return new_total

  #new_value is user_input,    current_total = inventory
 

def calculate_tax(amount):          #counts tax amount for each input
    tax = amount*tax_rate
    return tax

 
def generate_report(total_units, failed_attempts): #only supposed to print
    print(f"Total Deliveries Processed: {total_units}\nThe Number of Failed/Rejected Entries: {failed_attempts}")


def load_inventory():
    try:
        with open(inventory_file, "r") as file:
            inventory, *transactory_history = file
            inventory = int(inventory.strip())          #deletes "\n" & convert to integer
            transactory_history = [str(x.strip()) for x in transactory_history]     #spliting each value in transactory_history
    
    except FileNotFoundError:                           #if file doesn't exist
        inventory = 0
        transactory_history = []
    return inventory, transactory_history         #inventory = previous total   

        
def save_inventory(inventory, transactory_history):             #inventory = total inventory
    with open(inventory_file, "w") as file:
        transactory_history = [str(x) for x in transactory_history]     #spliting each value in transactory_history
        file.writelines(str(inventory) + "\n")
        file.write(str("\n".join(transactory_history)))                 #spliting each value in transactory_history


def main():
 
    inventory = 0
    tax_amount = 0
    exit_program = False
    failed_attempts = 0
    transaction_history = []
    
 
    while not exit_program:   #while True
        
        quantity, rejected_entries = get_valid_input()
        failed_attempts += rejected_entries             #internal counter for failed attempts from get_valid_input
        
        if load_inventory() == None:            #if inventory.txt doesn't exist, pass
            break
        else:
            inventory1, transaction_history = load_inventory()   #unpacking the tuple of load_inventory, inventory1 = previous history
            

        if quantity == "quit":                            
            generate_report(inventory, failed_attempts)           
            exit_program = True    
            break  
        
        else:
            result = process_delivery(inventory, quantity)              #inventory = current total; quantity = new total; result = total inventory
            
            if result == None:              #for any non-valid input & exceeded capacity
                failed_attempts += 1

            else:
                transaction_history.append(quantity)
                inventory = inventory1 + quantity
                tax_amount = calculate_tax(quantity)
                print(f"Tax for this delivery amount: {tax_amount}")      
                                     
        save_inventory(inventory, transaction_history)      #inventory = total
         

if __name__=="__main__":
    main()
    

