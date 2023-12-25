#!/usr/bin/python3

class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def talk(self):
        print("Hello, I am {}.".format(self.name))
        print("My roll no is {}.".format(self.rollno))
        print("My marks are {}.".format(self.marks))

s1 = Student("Sammy", 101, 90)
s1.talk()
