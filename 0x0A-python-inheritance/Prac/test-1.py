#!/usr/bin/python3

class Car:
    def __init__(self, name, model, colour):
        self.name = name
        self.model = model
        self.colour = colour

    def getInfo(self):
        print("Car name:{}, model:{}, colour:{}".format(self.name, self.model, self.colour))

class Employee:
    def __init__(self, ename, eno, car):
        self.ename = ename
        self.eno = eno
        self.car = car

    def empInfo(self):
        print("Employee name : ", self.ename)
        print("Employee number : ", self.eno)
        print("Employee car information")
        self.car.getInfo()


car = Car("Innova", "2.5V", "Grey")
emp = Employee("Durga", "872425", car)
emp.empInfo()
