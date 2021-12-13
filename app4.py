import datetime
import csv

class Item:
    '''
        build:
        - constructor + class attri.
        - methods (add/subtract quantity, reminders, total value )
        - magic method (__repr__)
        - alt. construc via @classmethod
        - getters
    '''
    refund_policy = 7
    all_instances = []

    def __init__(self, name: str, price: float, quantity: int, order_date = datetime.datetime.now() ):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__order_date = order_date

        self.all_instances.append(self)

    @property
    def order_date(self):
        print('hello from property')
        return self.__order_date

    @classmethod
    def from_csv(cls):

        with open('invoice1.csv') as file:
            list_dict = list(csv.DictReader(file))
        
        for item in list_dict:
            item = cls(
                name = item.get('name'),
                price = item.get('price'),
                quantity = item.get('quantity')
            )
            # cls.all_instances.append(item)
        return cls.all_instances
        

    def add_inventory(self, amount):
        self.quantity += amount
        return self.quantity

    def subtract_inventory(self, amount):
        self.quantity -= amount
        return self.quantity

    def reminder_refund(self):
        return f"Refund policy for  {self.name} applies for {self.refund_policy} days!"

    def total_value(self):
        total = self.price * self.quantity
        return total
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity}, {self.order_date})"

order1 = Item("Bonsai", 10.00, 10) 

# print(order1.from_csv()) 
# print(order1.all_instances)

# print(order1.quantity)
# print(order1.add_inventory(4))
# print(order1.reminder_refund())
# print(order1.total_value())
