# factorial_test.py

import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_positive():
    assert factorial(3) == 6
    assert factorial(5) == 120
    assert factorial(7) == 5040

def test_factorial_negative():
    # Add any additional test cases for negative scenarios
    pass
