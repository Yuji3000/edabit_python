# test_factorial.py
from challenges.factorial import factorial

def test_factorial_with_5():
    result = factorial(5)
    assert result == 120

def test_factorial_with_3():
    result = factorial(3)
    assert result == 6

def test_factorial_with_2():
    result = factorial(2)
    assert result == 2
