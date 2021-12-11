class Item:

    refund_duration = 20

    def __init__(self, name: str, price: float, quantity=0):
        
        assert price > 0, f"Provided price {price} is below $0"
        assert quantity >= 0, f"Provided quantity {quantity} has to be or above 0"

        self.name = name
        self.price = price
        self.quantity = quantity

    # update to inventory from delivery       
    @classmethod
    def from_delivery(cls,name,price,quantity):
        return cls(name,price,quantity)

    # alt const. for item from online orders       
    @classmethod
    def from_online_order(cls):
        # via json, list
        return cls()
        pass
    
    @staticmethod
    def branch(location):
        pass

    def add_to_inventory(self):
        pass

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

bonsai.refund_duration = 3

# print(bonsai)
# print(tempertourist)
# print(mixed_aquatic)

print(bonsai.__add__(tempertourist))

