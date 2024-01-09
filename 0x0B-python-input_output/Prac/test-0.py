#!/usr/bin/python3

f = open("abc.txt", "w")
print("Name : ", f.name)
print("Mode : ", f.mode)
print("closed : ", f.closed)
print("Is readable : ", f.readable())
print("Is writable : ", f.writable())
f.close
