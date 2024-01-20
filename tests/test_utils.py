import pytest

from veld.utils import parse_numeric


def test_parse_numeric_1():
    assert int(1) == parse_numeric("1")
    assert float(5.5) == parse_numeric("5.5")


def test_parse_numeric_2():
    with pytest.raises(ValueError):
        parse_numeric("a")
