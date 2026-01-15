import pytest

# reference fibonacci numbers, copied from wikipedia
fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21]

@pytest.mark.parametrize(('n', 'expected'), enumerate(fibs))
def test_fibonacci(n, expected):
    from fibonacci import fibonacci

    assert fibonacci(n) == expected
