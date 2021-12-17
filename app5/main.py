from store import Store

def main():

    Store1 = Store()

    Store1.create()
    # Store1.create()
    # Store1.create()
    Store1.add()
    # Store1.minus()
    print(Store1.orderDict)

if __name__=='__main__':
    main()