#!/usr/bin/python3

class Person(object):
    # constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)

# Driver code
emp = Person("Ekeno", 1883) # An object of a person
emp.Display()
