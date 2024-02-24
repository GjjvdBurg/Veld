#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for the max command

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

from pathlib import Path

from typing import List

import pytest

from tests.test_console.helpers import run_command


@pytest.mark.parametrize(
    ("values", "args", "expected"),
    [
        (
            [[1], [5], [6]],
            [],
            [[6]],
        ),
        (
            [[-1, 8], [5, 2], [6, -10], [8, 11]],
            [],
            [[8, 11]],
        ),
        (
            [[-1, 8], [5, 2], [6, -10], [8, 11]],
            ["--flatten"],
            [[11]],
        ),
        (
            [[-1, 8], [5, 2], [6, -10], [8, 11]],
            ["--reduce"],
            [[8], [5], [6], [11]],
        ),
    ],
)
def test_max(
    values: List[List[float]],
    args: List[str],
    expected: List[List[float]],
    tmp_path: Path,
) -> None:
    output = run_command("max", args, values, tmp_path)
    assert output == expected
