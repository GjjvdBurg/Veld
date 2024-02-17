#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for count operator

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import pytest

from typing import List, Any

from veld.core.operators import ModeOperator
from veld.core.operators import SingleResultContainer


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        (
            [4, 2, 8, 2],
            SingleResultContainer(2),
        ),
        (
            [4, 2, 8, 2, 1, 1],
            SingleResultContainer(1),
        ),
        (
            [4, 2, float("nan"), 2],
            SingleResultContainer(2),
        ),
        (
            ["a", "b", "b", "d"],
            SingleResultContainer("b"),
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
    operator = ModeOperator()
    for value in values:
        operator.update(value)
    assert operator.result == expected
