class Order:

    refund_dur = 7
    def __init__(self, name:str, price: int, quantity: int):
        self.name = name,
        self.price = price,
        self.quantity = int(quantity)
    
    def __repr__(self):
        return f"Order('{self.name}', {self.price}, {self.quantity}"

    def add_invt(self, amount):
        self.quantity += amount
        return f"Inventory increased to {self.quantity}"
        
    def minus_invt(self, amount):
        if self.quantity < 0:
            return "Check balance for sufficient funds"
        self.quantity -= amount
        return f"Inventory decreased to {self.quantity}"

    def reminder_refund(self):
        return f"refund policy is {Order.refund_dur}"