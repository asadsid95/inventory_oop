class Item:
    def __init__(self, name, price, quanity, totalQuantity):
        self.name = name
        self.price = price
        self.quanity = quanity
        self.totalQuantity = totalQuantity

phone = Item('Phone', 500, 10, 5000)
print(phone.name)
print(phone.quanity)
