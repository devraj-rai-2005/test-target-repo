"""
Pytest suite for src.math_utils module.
Covers add() and multiply() with positive, negative, and zero values.
"""

import pytest
from src.math_utils import add, multiply

# Tests for add()
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),          # both positive
        (-1, -2, -3),       # both negative
        (0, 5, 5),          # zero + positive
        (10, -4, 6),        # positive + negative
        (0, 0, 0),          # both zero
    ],
)
def test_add(a: int, b: int, expected: int) -> None:
    assert add(a, b) == expected

# Tests for multiply()
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),          # both positive
        (-2, 3, -6),        # negative * positive
        (0, 5, 0),          # zero * positive
        (-4, -5, 20),       # both negative
        (0, 0, 0),          # both zero
    ],
)
def test_multiply(a: int, b: int, expected: int) -> None:
    assert multiply(a, b) == expected
