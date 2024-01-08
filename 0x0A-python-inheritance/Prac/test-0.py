#!/usr/bin/python3
#class composition relationship

class Engine:
    def __init__(self):
        self.power = '123KW'

    def m1(self):
        print("Engine specific functionality")


class Car:
    def __init__(self):
        self.engine = Engine()

    def useEngine(self):
        print("Car requires engine")
        self.engine.m1()
        print(self.engine.power)

c = Car()
c.useEngine()
