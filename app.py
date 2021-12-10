class Item:

    refund_duration = 20

    def __init__(self, name: str, price: float, quantity=0):
        
        assert price > 0, f"Provided price {price} is below $0"
        assert quantity >= 0, f"Provided quantity {quantity} has to be or above 0"

        self.name = name
        self.price = price
        self.quantity = quantity
        

    def total_value(self):
        message = f"Inventory value for {self.name}: {self.price * self.quantity}"
        return message

    def reminder_refund(self):
        message = f"Remind customer: {self.name}'s refund policy is {self.refund_duration} day"
        return message

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

