#!/usr/bin/python3
#By Ekeno

class Tst:
    # Calling a constructor explicitly is not recommended
    def __init__(self):
        print("Check this")

t = Tst()   #one object created

#constructor executing like normal method when called called explicitly
t.__init__()
t.__init__()
t.__init__()
