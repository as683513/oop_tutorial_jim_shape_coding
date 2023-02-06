from item import Item

class Phone(Item):
    pay_rate = 0.5
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #call to super funtion to have access to parent class
        super().__init__(name, price, quantity)
        
        
        # run validations to recived arugments

        assert broken_phones >=0, f"Broken Phones {broken_phones} is not greater than or equal to zero."
        
        #assing to self object
        self.broken_phones = broken_phones
