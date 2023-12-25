#!/usr/bin/python3
#Created by Ekeno

class Student:
    """Test 0 by Ekeno"""
    def __init__(self):
        self.name = 'Ekeno'
        self.rollno = 1883
        self.marks = 93

    def talk(self):
        print(f"Hello, I am {self.name}.")
        print(f"My rollno is: {self.rollno}.")
        print(f"My marks are {self.marks}.")

s = Student()
print(s.name)
print(s.rollno)
s.talk()
