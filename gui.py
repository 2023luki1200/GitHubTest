# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:50:33 2024

@author: lukas
"""

from calc import call_func

## This code is the interface for the input

print("Hello to the Calculator")



print("Test")


def newinput(): ## Function will print a little instruction and then get the input for the operator and the two numbers.
    print("For addition 'a'")
    print("For subtract 's'")
    print("For multiply 'm'")
    print("For division 'd'")
    k=input("Your choice:")
    x=input("Number x:")
    y=input("Number y:")
    x=int(x)
    y=int(y)
    
    print(call_func(k,x,y))
    newinput()          # repeat the function after the last input or in case of an error

newinput()              ## starts the calculator