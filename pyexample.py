import pytest
import unit


def test_factorial(inputs):
     return unit.factor(inputs)

@pytest.mark.parametrize(" test_input, expected",[(3,6),(4,8)])
def test_function(test_input, expected):
    assert test_factorial(test_input) == expected  