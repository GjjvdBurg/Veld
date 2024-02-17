#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for summary operator

Author: G.J.J. van den Burg
Copyright: (c) 2024, G.J.J. van den Burg
License: See LICENSE file.

"""

import pytest

from typing import List

from veld.core.operators.summary import SummaryOperator
from veld.core.operators._container import SummaryResultContainer


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        (
            [1.0, 2.0, 3.0, 4.0, 5.0],
            SummaryResultContainer(
                count=5,
                maximum=5,
                minimum=1,
                mean=3,
                mode=1,
                total=15,
            ),
        ),
        (
            ['a', 'b', 'c', 'd', 'a', 'b', 'z'],
            SummaryResultContainer(
                count=7,
                maximum='z',
                minimum='a',
                mean=None,
                mode='a',
                total=None,
            ),
        ),
        (
            [],
            None,
        ),
    ],
)
def test_summary(
    values: List[float],
    expected: SummaryResultContainer,
) -> None:
    operator = SummaryOperator()
    for value in values:
        operator.update(value)
    assert operator.result == expected
