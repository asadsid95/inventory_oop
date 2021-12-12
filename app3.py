import datetime

class Plant:
    ''' 
    build:
    - constructor
    - alt. constructor(s)
    - methods for store use(receive, sell, reminders)
    - getter/setter use


'''
    refund_policy = 7

    def __init__(self, name, price=0.00, quantity=0, order_time = datetime.datetime.now()):
        self.name = name
        self.price = price
        self.quantity =  quantity
        self.order_time = order_time
        
    @classmethod
    def from_db(self):
        
        pass

    @classmethod
    def from_csv(self):

        pass

    @property
    def total_value(self):
        step = self.price * self.quantity
        return step
    
    def add_inventory(self, amount):
        self.quantity += amount

    def subtract_inventory(self, amount):
        self.quantity -= amount
    
    def reminder_refund(self):
        reminder = f"Refund policy applies for {self.refund_policy}"
        return reminder

order1 = Plant("Submerged", 30, 10)
order2 = Plant("Dry Surrounds", 40, 8)

print(order1.order_time)
print(order2.name)