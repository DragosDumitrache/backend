# Create your tests here.
from .calculations.mathematics import add_two_numbers


def test_addition_works():
    assert add_two_numbers(2, 2) == 4
