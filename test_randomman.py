from randomman import *

def test_correlation():
    assert correlation([1,2,3,4,],[4,5,6,7]) == 1
    assert correlation([1,2,3,4,],[7,6,5,4]) == -1