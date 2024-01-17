#!/usr/bin/python3
# Child classi
Person = __import__('test-4').Person


class Emp(Person):
    def Print(self):
        print("Emp classs called")

if __name__ == "__main__":

    Emp_details = Emp("Mayer", 1920)

    # calling parent class method 
    Emp_details.Display()

    # Calling child class method
    Emp_details.Print()
