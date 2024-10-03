import pytest

from veld.utils import parse_numeric


def test_parse_numeric_1():
    assert int(1) == parse_numeric("1")
    assert float(5.5) == parse_numeric("5.5")
    assert float(1e-3) == parse_numeric("1e-3")
    assert float(1.123e-13) == parse_numeric("1.123e-13")
    assert float(1.13e5) == parse_numeric("1.13e+5")


def test_parse_numeric_2():
    with pytest.raises(ValueError):
        parse_numeric("a")
