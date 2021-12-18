class Account:
    '''
        Each acc. should have name, amount & PIN
    '''
    def __init__(self, name, amount, pin):
        assert pin >= 1000, 'PIN must be 4-digits'

        self.name = name
        self.amount = int(amount)
        self.pin = int(pin)
        self.accTransactionDict = {} # add transaction history in account
    
    def add_money(self, amount):
        assert amount > 0, 'need Amount > 0'
        self.amount += amount
        return self.amount

    def minus_money(self, amount):
        assert amount > 0, 'need Amount > 0'
        
        if self.amount > 0:
            self.amount -= amount
            return self.amount
        else:
            return 'No sufficient funds'


# print(Account('Asad', 100, 111).add_money(100))
# print(Account('Asad', 100, 1111).minus_money(50))