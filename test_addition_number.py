import pytest

def test_add_numbers(x, y):
    return x+y


assert test_add_numbers(2, 3) == 5
assert test_add_numbers(5, 5) == 10
assert test_add_numbers(9, 10) == 19
assert test_add_numbers(-1, 1) == 0    