#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for cumsum command

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import pytest

from tests.test_console.helpers import run_command


@pytest.mark.parametrize(
    ("values", "args", "expected"),
    [
        (
            [[1], [3], [5]],
            [],
            [[1], [4], [9]],
        ),
        (
            [[1, 2], [3, 4], [5, 6]],
            [],
            [[1, 2], [4, 6], [9, 12]],
        ),
        (
            [[1, 2], [3, 4], [5, 6]],
            ["--flatten"],
            [[1], [3], [6], [10], [15], [21]],
        ),
    ],
)
def test_cumsum(values, args, expected, tmp_path) -> None:
    assert expected == run_command("cumsum", args, values, tmp_path)
