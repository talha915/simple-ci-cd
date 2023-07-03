import pytest
from addition_number import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(5, 5) == 10
    assert add_numbers(9, 10) == 19
    assert add_numbers(-1, 1) == 0    