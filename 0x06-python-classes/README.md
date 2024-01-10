## 0x06. Python - Classes and Objects
This directory contains solutions to tasks that introduce rudimentary concepts of Object-oriented programming.

## Resources
+ [intro to OOP](https://www.youtube.com/watch?v=ark2VQUZvAA&list=PLdtZyZnKFtadHJ2C1_-rKsmNA1RR5HzQT&index=1&pp=iAQB)
+ [__init__ constructor](https://www.youtube.com/watch?v=9hgBZYjCp3M&list=PLdtZyZnKFtadHJ2C1_-rKsmNA1RR5HzQT&index=2)

## Tasks

0. My first square:
An empty class ```Square``` that defines a square.

0. Square with size:
A class ```Square``` that defines a square.
	+ Private instance attribute: ```size```
	+ Instantiation with size (no type/value verification)

NB:Why ```size``` is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

0. Size Validation:
A class ```Square``` that defines a square.
	+ Private instance attribute: ```size```
	+ Instantiation with optional ```size: def __init__(self, size=0):```
		- size must be an integer, otherwise ```TypeError``` exception with the message ```size must be an integer``` is raised.
		- if size is less than 0, a ```ValueError exception``` with the message ```size must be >= 0``` is raised.

0. Area of a square:
A class ```Square``` that defines a square.
        + Private instance attribute: ```size```
        + Instantiation with optional ```size: def __init__(self, size=0):```
                - size must be an integer, otherwise ```TypeError``` exception with the message ```size must be an integer``` is raised.
                - if size is less than 0, a ```ValueError exception``` with the message ```size must be >= 0``` is raised.
	+ Public instance method: ```def area(self):``` that returns the current square area 
