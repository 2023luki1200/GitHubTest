# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 17:33:31 2024

@author: lukas
"""

from calculator import add 
from calculator import sub
from calculator import div
from calculator import mult
from calculator import mod

def test_add():
    
    assert add(1,1)==2
    assert add(-3,5)==2
    assert add(-1,-4)==-5
    

def test_sub():
    assert sub(1,1)==0
    assert sub(-3,5)==-8
    assert sub(-1,-4)==3
    
def test_mult():
    assert mult(1,1)==1
    assert mult(-3,5)==-15
    assert mult(-1,-4)==4
    
def test_div():
    assert div(1,1)==1
    assert div(-60,4)==-15
    assert div(-4,-1)==4
    assert div(1,2)==0.5
    
