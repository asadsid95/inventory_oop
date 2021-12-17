from order import Order

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
        order = str(input("Item name: "))
        price = float(input("Price: "))
        quantity = input("Quantity: ")
        self.orderCreated = Order(order, price, quantity) # POI
        self.orderDict[self.dictCounter] = self.orderCreated
        self.dictCounter += 1 

    def add(self):
        # input order number (key) to get Order object from dict{}
        print(self.orderDict)
        order_number = input("Order number to add inventory to: ")
        order_number=int(order_number)
        if order_number > self.dictCounter:
            return print(f"Order number {order_number} doesn't exist")
        add = input("How many would you like to add? ")
        add = int(add)

        order = self.orderDict[order_number].add_invt(add)

    def minus(self):
        # input order number (key) to get Order object from dict{}
        print(self.orderDict)        
        order_number = input("Order number to minus inventory from: ")
        if order_number not in self.orderDict:
            return print(f"Order number {order_number} doesn't exist")
        order_number=int(order_number)
        minus = input("How many would you like to take? ")
        minus = int(minus)

        order = self.orderDict[order_number].minus_invt(minus)

    def delete(self):
        order_number = input("Order number to remove: ")
        order_number = int(order_number)

        del self.orderDict[order_number]