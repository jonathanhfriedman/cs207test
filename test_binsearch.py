
from pytest import raises
from binsearch import binary_search

def test_nan():
    with raises(TypeError):
        binary_search([1, 2, float('nan')], 3)

def test_empty():
    assert binary_search([], 1) == -1
    
def test_one_element():
    assert binary_search([1], 1) == 0
    assert binary_search([1], 0) == -1
    
def test_larger():
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    
def test_smaller():
    assert binary_search([1, 2, 3, 4, 5], 0.5) == -1
    
def test_middle():
    assert binary_search([1, 2, 3, 4, 5], 3.5) == -1