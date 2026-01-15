import pytest
import math


def sinc(x):
    return math.sin(x) / x

def model(a, b, c):
    breakpoint()
    return sinc(a * (b - c))

def simulate(a, b):
    result = 0
    for c in range(5):
        result += model(a, b, c)
    return result


def test_simulate():
    assert simulate(a=1, b=10) == pytest.approx(0.16234459123220282)
    assert simulate(a=1, b=4) == pytest.approx(2.1539590770803776)
