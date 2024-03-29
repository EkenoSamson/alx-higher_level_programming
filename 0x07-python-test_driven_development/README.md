## 0x07. Python - Test-driven development

## Tasks

0. Integers addition
A function that add 2 integers.
	+ Prototype: ```def add_integer(a, b=98):```
	+ ```a``` and ```b``` must be integers or floats, otherwise raise a ```TypeError``` exception with the message ```a must be an integer or b must be an integer```
	+ ```a``` and ```b``` must be first casted to integers if they are float.
	+ Returns an integer: the addition of ```a``` and ```b```

0. Say my name
A function that prints ```My name is <first name> <last name>```
	+ Prototype: ```def say_my_name(first_name, last_name=""):```
	+ ```first_name``` and ```last_name``` must be strings otherwise, raise a ```TypeError``` exception with the message ```first_name must be a string``` or ```last_name must be a string```

0. Print square
A function that prints a square with the character #.
	+ Prototype: ```def print_square(size):```
	+ ```size``` is the size length of the square.
	+ ```size``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```size must be an integer```
	+ if ```size``` is less than ```0```, raise a ```ValueError``` exception with the message ```size must be >= 0```
	+ if ```size``` is a ```float``` and is less than ```0```, raise a ```TypeError``` exception with the message ```size must be an integer```

0. Text indeentation
A function that prints a text with 2 new lines after each of these characters: ```.```, ```?``` and ```:```.
	+ Prototype: ```def text_indentation(text):```
	+ ```text``` must be a string, otherwise raise a ```TypeError``` exception with the message ```text must be a string```
	+ There should be no space at the beginning or at the end of each printed line



