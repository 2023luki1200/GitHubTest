# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:58:02 2024

@author: lukas
"""

from calculator import add 
from calculator import sub
from calculator import div
from calculator import mult



def call_func(k,x,y):
    if(k=='a'):
        r=add(x,y)
    
    else:
        if(k=='s'):
            r=sub(x,y)
        else: 
            if(k=='m'):
                r=mult(x,y)
            else:
                if(k=='d'):
                    r=div(x,y)
                else:
                    r=("Error")
    return r

    