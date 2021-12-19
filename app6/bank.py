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
        self.accCounter = 0
        self.bankLedger = {} # not sure how to add this
        self.ledgerCounter = 0

    def create(self):
        # create account w/ user input
        name = input('Name of account holder: ')
        iAmount = input('Amount to open account with: ')
        pin = int(input('PIN: '))

        # store in accountLedger
        self.accountsLedger[self.accCounter] = Account(name, iAmount, pin)
        self.accCounter += 1

    def deposit(self):
        account_number = int(input(f'Pick an account number from {list(self.accountsLedger.keys())}: '))
        account = self.accountsLedger[account_number]

        amount = int(input('Amount to deposit: '))  
        return account.add_money(amount)

    def withdraw(self):
        account_number = int(input(f'Pick an account number from {list(self.accountsLedger.keys())}: '))
        account = self.accountsLedger[account_number]

        amount = int(input('Amount to withdraw: '))  
        return account.minus_money(amount)

    def close(self):
        acc_to_close = int(input(f"Pick an account number to close, from {list(self.accountsLedger.keys())}: "))
        del self.accountsLedger[acc_to_close]

        return self.accountsLedger

    def add_to_ledger(self):
        self.bankLedger[self.ledgerCounter] = self
        self.ledgerCounter += 1

        return f"Bank's ledger history: {self.bankLedger}"
