class StoreItem:
    pass
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

class Store:
    # Each object represents a store's inventory order's ledger 

    # able to create, store, find and change, and delete each order 
    # # lists can be used but what if client needs to delete from mid-list? It means all elements to-right have to be shifted
    
    def __init__(self):
        self.orderDict = {}
        self.dictCounter = 0

    def create(self):
        # new Order added to dict{}
        print("To add item in Store's inventory, do the following:")
        order = input("Item name: ")
        price = input("Price: ")
        quantity = input("Quantity: ")
        self.orderCreated = Order(order, price, quantity) # POI
        self.orderDict[self.dictCounter] = self.orderCreated
        self.dictCounter += 1 

    def add(self):

        # input order number (key) to get Order object from dict{}
        order_number = input("Order number: ")
        order_number=int(order_number)
        add = input("How many would you like to order? ")
        add = int(add)

        order = self.orderDict[order_number]
        changed_order = order.add_invt(add)
        print(changed_order)

        pass

    def minus(self):
        # input order number (key) to get Order object from dict{}
        order_number = input("Order number: ")
        order_number=int(order_number)
        minus = input("How many would you like to order? ")
        minus = int(minus)

        order = self.orderDict[order_number]
        changed_order = order.minus_invt(minus)
        print(changed_order)

    def delete(self):
        pass

## Main code below
order1 = Store()

order1.create()
# print(order1.orderDict)

order1.add()
order1.minus()
# print(order1.orderDict)