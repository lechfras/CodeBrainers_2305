import pytest
from pytest import approx

def quadratic(a, b, c):
    """Calculate roots of a quadratic function.
    https://en.wikipedia.org/wiki/Quadratic_function
    Quadratic function f(x) = ax^2 + bx + c
    Roots are defined as:
        x1 = (-b - sqrt(delta)) / 2a
        x2 = (-b + sqrt(delta)) / 2a
    when delta > 0,
        x0 = -b / 2a
    when delta = 0,
    and None otherwise.
    delta = b^2 - 4ac
    """
    # Protip: Use parentheses around arithmetic calculations!
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        return (-b - delta ** 0.5) / (2 * a), (-b + delta ** 0.5) / (2 * a)
    elif delta == 0:
        return -b / (2 * a)
    else:
        return None


# TESTS!

from pytest import approx

@pytest.mark.label1
def test_bez_pierwaistka():
    assert quadratic(1, 1, 2) == None
    assert quadratic(2, 2, 2) == None

@pytest.mark.label2
def test_jeden_pierwiastek():
    assert quadratic(1, 2, 1) == -1
    assert quadratic(4, -2, 0.25) == 0.25

@pytest.mark.label3
def test_dwa_pierwiastki():
    assert quadratic(2, 2, -1) == approx((-1.366, 0.366), 0.001)
    assert quadratic(2, -4, 1) == approx((0.293, 1.707), 0.001)

