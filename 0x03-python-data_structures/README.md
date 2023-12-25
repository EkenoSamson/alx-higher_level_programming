# 0x03. Python - Data Structures: Lists, Tuples

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

1. Why Python programming is awesome.
2. What are lists and how to use them.
3. What are the differences and similarities between strings and lists.
4. What are the most common methods of lists and how to use them.
5. How to use lists as stacks and queues.
6. What are list comprehensions and how to use them.
7. What are tuples and how to use them.
8. When to use tuples versus lists.
9. What is a sequence.
10. What is tuple packing.
11. What is sequence unpacking.
12. What is the `del` statement and how to use it.

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the pycodestyle (version 2.8.*).
- All your files must be executable.
- The length of your files will be tested using `wc`.

### C
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- All your files should end with a new line.
- Your code should use the Betty style. It will be checked using `betty-style.pl` and `betty-doc.pl`.
- You are not allowed to use global variables.
- No more than 5 functions per file.
- The prototypes of all your functions should be included in your header file called `lists.h`.
- Don’t forget to push your header file.
- All your header files should be include guarded.

## Tasks

### 0. Print a list of integers
Write a function that prints all integers of a list.

**Prototype:** `def print_list_integer(my_list=[]):`

**Format:** one integer per line.

### 1. Secure access to an element in a list
Write a function that retrieves an element from a list like in C.

**Prototype:** `def element_at(my_list, idx):`

If idx is negative, the function should return `None`.

### 2. Replace element
Write a function that replaces an element of a list at a specific position (like in C).

**Prototype:** `def replace_in_list(my_list, idx, element):`

If idx is negative, the function should not modify anything and return the original list.

### 3. Print a list of integers... in reverse!
Write a function that prints all integers of a list, in reverse order.

**Prototype:** `def print_reversed_list_integer(my_list=[]):`

**Format:** one integer per line.

### 4. Replace in a copy
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

**Prototype:** `def new_in_list(my_list, idx, element):`

If idx is negative, the function should return a copy of the original list.

### 5. Can you C me now?
Write a function that removes all characters 'c' and 'C' from a string.

**Prototype:** `def no_c(my_string):`

The function should return the new string.

*Note: You are not allowed to import any module or use `str.replace()`.*

Feel free to modify this README as needed for your project. Good luck!

