from item import Item

class Keyboard(Item):
    pay_rate = 0.7
    def __init__(self, name: str, price: float, quantity=0):
        #call to super funtion to have access to parent class
        super().__init__(name, price, quantity)
    