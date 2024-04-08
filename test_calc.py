from calc import call_func


def test_call_func():
    assert call_func('a', 1, 1) == 2
    assert call_func('s', -3, 5) == -8
    assert call_func('m', 1, 2) == 2
    assert call_func('d', 4, 2) == 2
    