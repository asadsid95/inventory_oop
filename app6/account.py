class Account:
    '''
        Each acc. should have name, amount & PIN
    '''
    def __init__(self, name, amount, pin):
        assert pin >= 1000, 'PIN must be 4-digits'

        self.name = name
        self.amount = int(amount)
        self.pin = int(pin)
        self.accTransactionsDict = {} # add transaction history in account
        self.counter = 0

    def __repr__(self):
        return f'Account({self.name},{self.amount})'

    def add_money(self, amount):
        assert amount > 0, 'need Amount > 0'

        self.amount += amount
        self.add_to_transactionHistory()
        print("Account history: ", self.accTransactionsDict)
        return self.amount

    def minus_money(self, amount):
        assert amount > 0, 'need Amount > 0'
        
        if self.amount > 0:
            self.amount -= amount
            self.add_to_transactionHistory()
            return self.amount
        else:
            return 'No sufficient funds'

    def add_to_transactionHistory(self):
        # saving each transaction's record by saving each with unique number
        # remember I can call a method inside another method
        self.accTransactionsDict[self.counter] = self
        self.counter += 1
        # how to save transaction with the action (add/minus) & show the amount changed by

        return f"Transactions history: {self.accTransactionsDict}"