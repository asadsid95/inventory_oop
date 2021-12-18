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
        pin = int(input('PIN: '))

        # store in accountLedger
        self.accountsLedger[self.counter] = Account(name, iAmount, pin)
        self.counter += 1

    def deposit(self):
        print(self.accountsLedger)
        account_number = int(input('Account number: '))
        account = self.accountsLedger[account_number]

        amount = int(input('Amount to deposit: '))  
        return account.add_money(amount)


    def withdraw(self):
        pass

    def close(self):
        pass

    def add_to_ledger(self):
        pass