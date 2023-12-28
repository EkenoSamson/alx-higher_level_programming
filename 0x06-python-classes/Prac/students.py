#!/usr/bin/python3
# By Ekeno

class Student:
    """
    Student information
    """
    school_name = "Saint Cosmas"

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def getStudentInfo(self):
        print("Student name: ", self.name)
        print("Student rollno: ", self.rollno)

    @classmethod
    def getSchoolInfo(cls):
        print("School name is :", cls.school_name)

    @staticmethod
    def getSum(a, b):
        return (a + b)

