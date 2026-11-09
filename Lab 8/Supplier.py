class Supplier:
    def __init__(self, supplier_id: str, supplier_name: str, contact_email: str):
        self.__supplier_id = supplier_id
        self.__supplier_name = supplier_name
        self.__contact_email = contact_email
    
    def valid_input(self) -> bool:
        if not self.__supplier_id or not self.__supplier_name or not self.__contact_email:
            return False
        else:
            return True
        
    def get_supplier_id(self) -> str:
        return self.__supplier_id
    
    def get_supplier_name(self) -> str:
        return self.__supplier_name
    
    def get_contact_email(self) -> str:
        return self.__contact_email
    
    def display_information(self) -> None:
        print(f"\nSupplier ID: {self.get_supplier_id()}, Name: {self.get_supplier_name()}, Contact Email: {self.get_contact_email()}")
    
    def get_fulfilment_info(self) -> str:
        return "Requires supplier information."
