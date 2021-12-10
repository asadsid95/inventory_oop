class Item:
    
    refund_limit_days = 30
    watering_period = 10   
     
    def __init__(self, name:str, price:float, quantity:int):
        
        assert price > 0, f"Price needs to be higher than $0"

        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
            totalValue = self.price * self.quantity 
            return totalValue

    def reminder_refund(self):
        print(f"Remind the Customer: {Item.refund_limit_days} days is the refund limit!")
        pass

    def reminder_watering(self):
        print(f"Remind the Customer: {self.name} needs to be watered every {self.watering_period} days!")
        # pass

bon = Item('Bonsai', 500.00, 10) # not sure why data type isnt enforced; look at __init__ attri.
aq = Item('Mixed Aquatic', 300.00, 9) 
t = Item('Temperatourist', 100.00, 10) # not sure why data type isnt enforced; look at __init__ attri.

# print(bon.total_value())
# print(bon.refund_limit_days)
# print(aq.total_value())
# print(aq.refund_limit_days)
# print(t.total_value())
# print(t.refund_limit_days)

bon.watering_period = 7
bon.refund_limit_days = 15 

# print(bon.watering_period)
print(bon.refund_limit_days)

# bon.reminder_watering()
