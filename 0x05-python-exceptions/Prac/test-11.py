#!/usr/bin/python3
#case 3 : exception rasied but not handled

try:
    print("try")
    print(10/0)
except ValueError:
    print("Except")
finally:
    print("finally")
