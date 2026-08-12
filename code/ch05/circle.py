# The circle module has functions that perform
# calculations related to circles.
import math
import pytest


# The area function accepts a circle's radius as an
# argument and returns the area of the circle.
def area(radius):
    """
    Given the radius of some circle, calculate and return the area
    of the circle.

    Parameters
    ----------
    radius : float
        The radius of a circle we are being asked to calculate
        the area for.

    Returns
    -------
    area : float
        The area of the indicated circle is calculated and returned
        as the result of this function.
    """
    return math.pi * radius**2


# The circumference function accepts a circle's
# radius and returns the circle's circumference.
def circumference(radius):
    """
    Given the radius of some circle, calculate and return
    the circumference around the circle.

    Parameters
    ----------
    radius : float
        The radius of a circle we are being asked to calculate
        the circumference for.

    Returns
    -------
    circumference : float
        The circumference of the indicated circle is calculated and
        returned as the result of this function.
    """
    return 2 * math.pi * radius


# example of pytest tests
def test_zero():
    a = area(0.0)
    assert a == pytest.approx(0.0)


def test_unit_circle():
    a = area(1.0)
    assert a == pytest.approx(0.0)


def test_small_circle():
    a = area(0.5)
    assert a == pytest.approx(0.7853981633974483)
