class Ship():
    def __init__(self, type, price):
        self.__type = type
        self.__price = price
    
    def get_ship_properties(self):
        print(f'The type of ship is {self.__type}')
        print(f'The price of the ship is ${self.__price}')

    def change_type(self, type):
        self.__type = type
    
    def change_price(self, price):
        self.__price = price


def func(obj): 
    obj.get_ship_properties()


ship = Ship("Kapal Motor", 1000)
func(ship)
ship.change_price(5000)
ship.change_type("Kapal Layar")
print("======After change properties======")
func(ship)
