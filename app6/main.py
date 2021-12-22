'''
Build a banking system for everyday use

Questions:
- capabilites/features?
    a. Deposit/Withdraw for multiple acc./users
    b. History of transactions per bank sys.
    c. Multiple bank instances
    d. Each bank has a initial amount to start with

'''
from bank import Bank

def main():
    bank1 = Bank()
    print(bank1.create())
    print(bank1.deposit())
    # print(bank1.close())

if __name__=='__main__':
    main()