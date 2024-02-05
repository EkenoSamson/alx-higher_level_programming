#!/usr/bin/env python3
# Fibonacci numbers module

def fib(n):
    """wrtie fibonacci numbers upto n"""
    a, b = 0, 1
    
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
    print()

def fib2(n):
    """return Fibonacci series upto n"""
    result = []
    a, b = 0, 1

    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
