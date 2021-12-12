# class for items to be in inventory for a store
# capabilities: +/- quantity, reminder about refund policy & watering

import csv

class Plant():

    refund_policy = 30
    watering_period = 10
    all_objects = []

    def __init__(self, name: str, price: float, quantity = 5):
        self._name = name
        self._price = price
        self.quantity = quantity

    @classmethod
    # alt constructor in case input is from csv file
    def from_csv(cls):
        
        with open("invoice1.csv") as file:
            invoice = list(csv.DictReader(file))
            
            for item in invoice:
                plant = Plant(
                    name = item.get('name'),
                    price = float(item.get('price')),
                    quantity= item.get('quantity')
                )
                Plant.all_objects.append(plant)

    @property
    # Name of item is read-only
    def name(self):
        return self._name

    @property
    # Price of item is read-only
    def price(self):
        return self._price

    def add_quantity(self, amount):
        self.quantity += amount
        pass

    def subtract_quantity(self, amount):
        self.quantity -= amount
        pass

    def total_value(self):
        total = self._price * self.quantity
        return total

    def reminder_refund(self):
        return f"Reminder: Refund policy applies for {self.refund_policy} days!"

    def reminder_watering(self):
        return f"Reminder: {self.name} needs to be watered every {self.watering_period} days!"

    def __repr__(self):
        return f"Plant('{self.name}', {self.price}, {self.quantity})"

plant1 = Plant("Bonsai", 54.99, 7)
plant2 = Plant("Cactii", 34.99, 8)
plant3 = Plant("Bamboo", 24.99, 8)

print(plant2.total_value())

# Plant.from_csv()
# print(Plant.all_objects)

