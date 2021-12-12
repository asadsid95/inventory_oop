# inventory system for a shop
# - able to add/subtract quantity, give reminders; adding is done via various sources (i.e. GUI user input, DB, ), 

import datetime
import csv

class Plant:
    ''' 
    build:
    - constructor
    - methods for store use(receive, sell, reminders)
    - __repr__
    - alt. constructor(s)
    - getter/setter use

'''
    refund_policy = 7
    all_instances = []

    def __init__(self, name, price=0.00, quantity=0, order_time = datetime.datetime.now()):
        self.name = name
        self.price = price
        self.quantity =  quantity
        self.order_time = order_time

        self.all_instances.append(self)
        
    @classmethod
    def from_db(self):
        
        pass

    @classmethod
    # alt. constrc 
    def from_csv(cls):
        
        with open("invoice1.csv") as invoice:
            invoice_listdict = list(csv.DictReader(invoice))
        
        for item in invoice_listdict:
            order = cls(
                name = item.get('name'),
                price = item.get('price'),
                quantity = item.get('quantity')
            )
            Plant.all_instances.append(order)
        # add to db from here??

        return Plant.all_instances 

    @property
    def total_value(self):
        total_value = self.price * self.quantity
        return total_value
    
    def add_inventory(self, amount):
        self.quantity += amount
        return self.quantity

    def subtract_inventory(self, amount):
        self.quantity -= amount
        return self.quantity

    def reminder_refund(self):
        reminder = f"Refund policy applies for {self.refund_policy}"
        return reminder

    def __repr__(self):
        return f"Plant('{self.name}', {self.price}, {self.quantity}, {self.order_time}"

order1 = Plant("Submerged", 10, 10)
order2 = Plant("Dry Surrounds", 40, 8)

print(order1.add_inventory(3))
print(order1.total_value)
print(order1.from_csv())
# print(order1.all_instances)


# print(order1.__class__.__name__)
# print(order2.from_csv())
# print(order2.all_instances)