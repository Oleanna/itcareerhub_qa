import pytest
from homework.simple_math import SimpleMath

@pytest.fixture
def math():
    return SimpleMath()


@pytest.mark.parametrize("input_value,expected", [
    (2, 4),
    (5, 25),
    (10, 100),
    (-2, 4),
    (-5, 25),
    (-10, 100),
    (0, 0),
])
def test_square(math, input_value, expected):
    assert math.square(input_value) == expected

@pytest.mark.parametrize("input_value,expected", [
    (2, 8),
    (3, 27),
    (4, 64),
    (-2, -8),
    (-3, -27),
    (-4, -64),
    (0, 0),
])
def test_cube(math, input_value, expected):
    assert math.cube(input_value) == expected
