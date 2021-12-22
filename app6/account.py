from DBcm import UseDatabase

class Account:
    '''
        Each acc. should have name, amount & PIN
    '''

    config_db = {'database': 'bank.db'}

    def __init__(self, name, amount, pin):
        assert pin >= 1000, 'PIN must be 4-digits'

        self.name = name
        self.amount = int(amount)
        self.pin = int(pin)
        self.accTransactionsDict = {} # add transaction history in account
        self.counter = 0

        with UseDatabase(Account.config_db) as self.cursor:
            create_table = '''CREATE TABLE IF NOT EXISTS account  (
                name text,
                amount real,
                pin integer
            )
            '''
            add_account_db = f'''
                INSERT INTO account (name, amount, pin) VALUES ('{self.name}', {self.amount}, {self.pin}) 
            '''
            self.cursor.execute(create_table)
            self.cursor.execute(add_account_db)

    def __repr__(self):
        return f'Account({self.name},{self.amount})'

    def add_money(self, amount):
        assert amount > 0, 'need Amount > 0'

        self.amount += amount
        with UseDatabase(Account.config_db) as self.cursor:
            amount_db = f'''UPDATE account
                SET amount = {self.amount}
                where name = '{self.name}' 
            '''
            self.cursor.execute(amount_db)

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