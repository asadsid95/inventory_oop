import csv
import datetime

class Item:

    refund_duration = 20
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        
        assert price > 0, f"Provided price {price} is below $0"
        assert quantity >= 0, f"Provided quantity {quantity} has to be or above 0"

        self.name = name
        self.price = price
        self.quantity = quantity

    @classmethod
    # alt const. for item from delivery       
    # imagine items needs to be created from csv (delivery company happens to send invoice in csv)
    def from_delivery(cls):

        with open('invoice1.csv') as invoice:
            content_invoice_reader = csv.DictReader(invoice) # Better than using reader() b/c dict is better to use in this case than list
            content_invoice = list(content_invoice_reader)
        
        for line in content_invoice:
            item = Item(  # this is same as creating items using Item(name, price, quantity)
                name = line.get('name'), 
                price = float(line.get('price')), 
                quantity = int(line.get('quantity')) 
            )
            Item.all.append(item)

    @classmethod
    # alt const. for item from online orders       
    # via json, list
    def from_online_order(cls):
        # return cls()
        pass
    
    # think of a utility function that can benefit the class
    # @staticmethod
    # def branch(location):
    #     pass

    # change quantity by amount
    def add_inventory(self, amount):
        self.quantity += amount
        return self.quantity

    # change quantity by amount
    def subtract_inventory(self, amount):
        self.quantity -= amount
        return self.quantity

    def total_value(self):
        message = f"Inventory value for {self.name}: {self.price * self.quantity}"
        return message

    def reminder_refund(self):
        message = f"Remind customer: {self.name}'s refund policy is {self.refund_duration} days!"
        return message

    # readable rep of object
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
    
    # Total cost of 2 items
    def __add__(self, other):
        sum = (self.price * self.quantity) + (other.price * other.quantity) 
        return sum


bonsai = Item('Bonsai', 500, 10)
tempertourist = Item("Tempertourist", 250, 10)
mixed_aquatic = Item("Mixed Aquatics", 100)

# print(bonsai.__add__(tempertourist))
# print(bonsai + tempertourist)

#####################
# This could be place where methods are called to imitate a store

print(Item.from_delivery()) # adding items received from delivery
print(Item.all)
# print(Item.from_online_order()) # adding items received from online order

print(bonsai.add_inventory(4)) # Use case: on screen option as item being checked in  
print(bonsai.subtract_inventory(8)) # Use case: on screen option as item being checked out 
 