# Inventory system

### Purpose

Create a program that allows user to track inventory details about various products offered by store
- details include: item type, price, quantity and total value

It would be connected to PoS, allowing purchasing of goods

------
#### Notes:
1. Constructors are used to create objects w/ fixed # of attributes (attri.). These are called Object attributes
- Setting their default values
- Setting data types for each attri. to ensure incorrect data types are passed
- Adding additional attri. into an object
- Putting validations for object attri's values (statement keyword assert)
2. Class attributes are defined in class-level (outside of `__init__`)
- Also notice the lack of `self.`
- When mentioned with an object, program will first search object's attribute and if not found, it will then check class-level for it
3. Magic method `__dict__`  zA  