import pytest

from solve_sqrt import Main
# temporarily removed

def test_sqrt():
    main = Main()
    assert main.calc_sqrt(9) == 3
