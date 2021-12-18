from account import Account

class Bank:
    '''
    Services provided:
        - create and close accounts
        - deposit/withdraw amount
        - keep track of all transactions
    '''
    def __init__(self) -> None:
        self.accountsLedger = {}
        self.counter = 0
        self.transactionsLedger = {} # not sure how to add this

    def create(self):
        # create account w/ user input
        name = input('Name of account holder: ')
        iAmount = input('Amount to open account with: ')
        pin = input('PIN: ')

        self.accountLedger[self.counter] = Account(name, iAmount, pin)
        self.counter += 1

    

        # store in accountLedger


        pass

    def deposit(self):
        pass

    def withdraw(self):
        pass

    def close(self):
        pass

    def add_to_ledger(self):
        pass