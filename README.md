# Inventory system

### Purpose

Create a program that allows user to track inventory details about various products offered by store
- details include: item type, price, quantity and total value

It would be connected to PoS, allowing purchasing of goods
- display reminders for client
- show total value of items
- addition/subtraction of quantities

Next areas to focus on:
- Since current flow of item happens on single-item basis, what if we could check out/in multiple items at once
- Organization in an inventory is valueable. What if grouping items to imitate aisles-like structure
- Adding more features to the inventory
------
#### Notes:
1. _Constructors_ are used to create objects w/ fixed # of attributes (attri.). These are called Object attributes
- Setting their default values
- Setting data types for each attri. to ensure incorrect data types are passed
- Adding additional attri. into an object
- Putting validations for object attri's values (statement keyword assert)

2. _Class attributes_ are defined in class-level (outside of `__init__`)
- Also notice the lack of `self.`
- When mentioned with an object, program will first search object's attributes for it and if not found, it will then check class-level
- **Use case**: attributes that remain same for all objects (refund policy)

3. _Magic method_ `__repr__`, `__add__`   
- Need to find a use for using these (less priority)
- **Use case** : used to customize objects to behave like built-in types 
- - Adding 2 class objects (non-built) would normally result in error as program doesn't know how to but defining function inside `__add__` could give that ability    
- __contains__ to check if element in object's container (list, tuples)
- to get class's name while inheriting, using `__class___.__name__` inside `__repr`

4. _Class method_ (takes the class itself as first arg & has access to class attri... therefore has access to class state)
- **Use case**: used to create factory methods (i.o.w., it returns object / i.o.w., alt. constructor)

5. _Static method_ (doesn't have access to class or object state -- Remember state = attribute & behaviour = method )
- Use to create utility methods
- also used during testing b/c independent methods (from class) can be inserted
- also for other maintenance-related features 

6. _getters setters_ (@property & @attri.setter)
- **Use case**: data encapsulation, to prevent direct access; way around not having private-hidden fields 
- any code placed within getter/setter will execute prior to returning property's value
- - think of putting conditional prior to setting property's value

7. Context management protocol: __enter__ & __exit__
