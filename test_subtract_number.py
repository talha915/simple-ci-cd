import pytest
from subtract_number import subtract

def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(5, 2) == 3