## 0x05. Python - Exceptions

0. safe list printing
A function that prints x elements of a list. All elements must be printed on the same line followed by a newline.
	+ prototype ``` def safe_print_list(my_list=[], x=0):```.
	+ x represents the number of elements to print. ``` 0 <= x ```.
	+ Return : the real number of elements printed.

0. Safe printig of an integer list:
A function that prints an integer with ```"{:d}".format()```.
	+ Prototype : ``` def safe_print_integer(value) ```
	+ Value - can be any type. (integer, string etc).
	+ The should be printed followed by a new line.
	+ Return: ``` True ``` if integer value has been correctly printed.

0. Print and count integer.
A function that prints the first x elements of a list and only integer.
	+ Prototype : ``` def safe_print_integers(my_list=[], x=0): ```.
	+ All integers have to beprinted on the same line followed by a new line - other type of value in the list must be skipped (silence).

0. Integer division with debug:
A function that divides 2 integers and prints the result.
	+ Prototype : ``` def safe_print_division(a, b): ```.
	+ Assumption: ```a``` and ```b``` are integers.
	+ Finally: contains result of division.
	+ Returns: the value of division; otherwise ``` None ```

0. Divide a list:
A fucntion that divides element by element 2 lists.
	+ Prototype ```def list_division(my_list_1, my_list_2, list_length): ```.
	+ ```list_length``` can be bigger than the length of both list.
	+ Return: a new list.
	+ if 2 elements can't be divided, the division result should be equal to zero.
	+ if an element is not an integer/ float: ```wrong type``` is typed.
	+ if the division can't be divided by zero: ```division by 0```.
	+ if ```my_list_1``` or ```my_list_2``` is too short : ```out of range```.

0. Raise exception:
A function that raises a type exception.
	+ Prototype : ```def raise_exception():```.

0. Raise a message:
A function that raises a name exception with a message.
	+ Prototype : ```def raise_exception_msg(message=""):```.
