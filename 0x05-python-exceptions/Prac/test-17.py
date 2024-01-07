#!/usr/bin/python3

f = None
try:
    f = open('abc.txt')
except:
    print("some prblem encountered while locating/ openning a file")
else:
    print("File opened successfully")
    print("The content of the file")
    print("#" * 30)
    print(f.read())
finally:
    if f is not None:
        f.close()
