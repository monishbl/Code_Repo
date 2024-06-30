# Solution for a question from Hakerrank - Python Basics
"""
Implement class: Vending Machine according to the following requirements:

• can be instantiated using the constructor Vending Machine num_items, item_price) where num items denotes the number of items in the machine, and item_price denotes the
required number of coins to buy a single item. has a method buyreq items, money) that represents a buy request where req_items denotes the requested number of items, and 
money is the amount the customer puts into the machine. Depending on the state of the machine, one of the following happens

o If there are enough items in the machine to serve the request and the given money is sufficient to buy the requested number of items, the number of items in the machine 
is reduced by the requested number of items. The method returns an integer denotes the change given back after the purchase. If there are fewer items in the machine than 
the requested number, it raises a ValueError exception with the message "Not enough items in the machine". If there are enough items in the machine to serve the request
but the given amount of money is less than their cost. It raises a ValueError exception with the message "Not enough coins". 

"""
class Machine():
    def __init__(self, items, price):
        self.items = items
        self.price = price
        self.change = 0

    def vend(self, quantity, money):
        if self.items == 0:
            return "Machine is out of stock."
        elif money < self.price*quantity:
            return "Not enough money!"
        elif quantity > self.items:
            return "Not enough stock!"
        else:
            self.items -= quantity
            self.change = money - self.price
            return "Here is your change of {} and your {} item(s).".format(self.change, quantity)



machine = Machine(5, 10)

print(machine.vend(2, 10))
print(machine.vend(2, 5))
print(machine.vend(2, 10))
print(machine.vend(2, 20))