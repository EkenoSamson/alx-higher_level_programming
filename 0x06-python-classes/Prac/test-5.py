#!/usr/bin/python3
#By Ekeno

class Student:
    def __init__(self, name, rollno, marks):
        print("Creating instances and initializations ...")
        self.name = name
        self.rollno = rollno
        self.marks = marks

s1 = Student("Sophiaa", 1399, 76)
print(s1.name, s1.rollno, s1.marks)
s2 = Student("Mariko", 1234, 89)
print(s2.name, s2.rollno, s2.marks)

