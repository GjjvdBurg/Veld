#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for count operator

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

from typing import Any
from typing import List

import pytest

from veld.core.operators import CountOperator
from veld.core.operators import SingleResultContainer


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        (
            [4, 8, 2],
            SingleResultContainer(3),
        ),
        (
            [4, 8, float("nan"), 2],
            SingleResultContainer(3),
        ),
        (
            ["a", "b", "c", "d"],
            SingleResultContainer(4),
        ),
        (
            [],
            None,
        ),
    ],
)
def test_count(
    values: List[Any],
    expected: int,
) -> None:
    operator = CountOperator()
    for value in values:
        operator.update(value)
    assert operator.result == expected
