# Inventory system

### Purpose

Create a program that allows user to track inventory details about various products offered by store
- details include: item type, price, quantity and total value

It would be connected to PoS, allowing purchasing of goods
- display reminders for client
- show total value of items
- addition/subtraction of quantities

0------
#### Notes:
1. Constructors are used to create objects w/ fixed # of attributes (attri.). These are called Object attributes
- Setting their default values
- Setting data types for each attri. to ensure incorrect data types are passed
- Adding additional attri. into an object
- Putting validations for object attri's values (statement keyword assert)

2. Class attributes are defined in class-level (outside of `__init__`)
- Also notice the lack of `self.`
- When mentioned with an object, program will first search object's attributes for it and if not found, it will then check class-level
- **Use case**: attributes that remain same for all objects (refund policy)

3. Magic method `__repr__`, `__add__`   
- Need to find a use for using these (less priority)
- **Use case** : __contains__ to check if element in object's container (list, tuples)

4. Class method (takes the class itself as first arg & can call class attri)
- Need to find a use for using these
- **Use case**: 
- - creates factory methods () return object
- - alt. constructors

5. Static method (takes neither)
- creating utility methods