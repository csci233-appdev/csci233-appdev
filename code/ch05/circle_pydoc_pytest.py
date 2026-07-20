import math
import pytest

# The sum function accepts two numeric arguments and
# returns the sum of those arguments.
def area_of_circle(radius):
    """
    Given the radius of some circle, calculate and return the area
    of the circle.

    Parameters
    ----------
    radius : float
        The radius of a circle we are being asked to calculate the area
        for.

    Returns
    -------
    area : float
        The area of the indicated circle is calculated and returned as the
        result of this function.  Area of a circle is $a = \\pi r^2$
    """
    area = math.pi * radius**2.0
    return area

# example of pytest tests
def test_zero():
    area = area_of_circle(0.0)
    assert area == pytest.approx(0.0)

def test_unit_circle():
    area = area_of_circle(1.0)
    assert area == pytest.approx(math.pi)

def test_small_circle():
    area = area_of_circle(0.5)
    assert area == pytest.approx(0.7853981633974483)
