## 0x0A. Python - Inheritance

## Resources

[Inheritance in Python](https://www.geeksforgeeks.org/inheritance-in-python/)


## Tasks

0. Look up
A function that returns the list of available attributes and methods of an object.
	+ Prototype: ``` def lookup(obj):```
	+ Return: list object.

0. My list
A class MyList that inherits from list:
	+ Public instance method: ```def print_sorted(self):``` that prints the list, but sorted (ascending sort).
	+ Assume that all the elements of the list will be of type int.

0. Exact same object
A function that returns True if the object is exactly an instance of the specified class ; otherwise False.
	+ Prototype: ```def is_same_class(obj, a_class):```

0. Same class or inherited
A function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
	+ Prototype: ```def is_kind_of_class(obj, a_class):```

0. Only sub class of
A function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
	+ Prototype: ```def inherits_from(obj, a_class):```
