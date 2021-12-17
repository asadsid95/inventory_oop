class StoreItem:
    
    '''
    
    building the class in order of:
    - constrc.
    - methods
    - class attri.
    - magic func. 
    - alt. constrc.
    - testing/maintenance methods

    how to expand using inheritance

    '''


class Order:

    refund_dur = 7
    def __init__(self, name, price, quantity):
        self.name = name,
        self.price = price,
        self.quantity = quantity
    
    def add_invt(self, amount):
        self.quantity += amount
        
    def minus_invt(self, amount):
        if self.quantity < 0:
            return "Check balance for sufficient funds"
        self.quantity -= amount

    def reminder_refund(self):
        return f"refund policy is {Order.refund_dur}"

class Store:
    # able to create, store, find and change, and delete each order 
    # # lists can be used but what if client needs to delete from mid-list? It means all elements to-right have to be shifted
    def __init__(self):
        self.orderDict = {}

    def create(self):
        # new Order
        
        order = input("Item name: ")
        price = input("Price: ")
        quantity = input("Quantity: ")
        self.orderCreated = Order(order, price, quantity) # POI
        self.orderDict['some counter'] = self.orderCreated

    def add(self):
        # input order number (key name
        pass

    def minus(self):
        pass

    def delete(self):
        pass

## Main code below
order1 = Store()
order1.create()
print(order1.orderDict)