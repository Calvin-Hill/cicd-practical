import pytest
from src.feature_practical_reza import evaluate_square


def test_accurate_evaluate_square():
    num = 2
    assert evaluate_square(num) == 'The square of 2 is 4'

