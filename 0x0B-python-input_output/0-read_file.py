#!/usr/bin/python3
# By Ekeno

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            print(line, end="")
