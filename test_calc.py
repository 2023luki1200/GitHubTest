# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 18:34:29 2024

@author: lukas
"""


from calc import call_func


def test_call_func():
    """Test for the call_func, with all different function and error return"""

    assert call_func('a', 1, 1) == 2
    assert call_func('s', -3, 5) == -8
    assert call_func('m', 1, 2) == 2
    assert call_func('d', 4, 2) == 2
    assert call_func('j', 1, 1) == "Error"
