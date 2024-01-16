#!/usr/bin/python3
# super concept in inheritance

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def eatndrink(self):
        print("Eat Biryani and drink Beer")
    
class Employee(Person):
    def __init__(self, name, age, eno, esal):
        #self.name =  name
        #self.age = age
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal

    def work(self):
        print("Codes Python projects")

    def empInfo(self):
        print(self.name)
        print(self.age)
        print(self.eno)
        print(self.esal)

e = Employee("Durga", 48, 872425, 10000)
e.eatndrink()
e.work()
e.empInfo()
