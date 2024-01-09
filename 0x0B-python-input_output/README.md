## 0x0B. Python - Input/Output

## Tasks

0. Read file:
A function that reads a text file(UTF8) and prints it to the stdout.
	+ Prototype : ``` def read_file(filename=""): ```.
	+ Must use ```with``` statement.
	+ No need to manage:  ``` file permission ``` and ```file doesn't exist``` exceptions.

0. Write to a file:
A function that write a string to a text file (utf-8).
	+ Prototype : ```def write_file(filename="", test=""):```.
	+ Must use the ```with``` statement.
	+ Overwrite, create if does not exist.
	+ Returns: the number of characters written.

0. Append to a file:
A function that appends a string at the end of a text file (utf-8).
	+ Prototype : ```def append_write(filename="", text=""):```.
	+ Returns: the number of characters addded.

0. To JSOn string.
A function that returns the JSON representation of an object(string).
	+ Prototype : ```def to_json_string(my_obj):```.

0. From JSON string to object:
A function that returns an object (Python data structure) represented by JSON string:
	+ Prototype : ```def from_json_string(my_str):```.

