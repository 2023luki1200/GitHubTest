# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:50:33 2024

@author: lukas
"""

from calc import call_func

print("Hello to the Calculator")



print("Test")


def newinput():
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
    newinput()

newinput()