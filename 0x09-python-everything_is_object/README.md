## 0x09. Python - Everything is object

0. who am I  
	- A function used to get the function of an object.
	- soln: type()
1. Where are you
	- A function used to get the variable identifier.
	- which is the memory address in the CPython implementation.
	- soln: id()
2. Right count
	- In following ``` >>> a = 89 ``` and ``` >>> b = 100 ```.
	- Do ``` a ``` and ``` b ``` point to the same object?
	- soln: ``` No ```
2. Right count
        - In following ``` >>> a = 89 ``` and ``` >>> b = 89 ```.
        - Do ``` a ``` and ``` b ``` point to the same object?
        - soln: ``` Yes ```
2. Right count
        - In following ``` >>> a = 89 ``` and ``` >>> b = a ```.
        - Do ``` a ``` and ``` b ``` point to the same object?
        - soln: ``` Yes ```
2. Right count
        - In following ``` >>> a = 89 ``` and ``` >>> b = a + 1 ```.
        - Do ``` a ``` and ``` b ``` point to the same object?
        - soln: ``` No ```
