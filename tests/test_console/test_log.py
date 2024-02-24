#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for log command

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
            [[1], [2], [3]],
            [],
            [[0.0], [0.6931471805599453], [1.0986122886681098]],
        ),
        (
            [[21], [22], [23]],
            ["-b", "10"],
            [
                [1.322219294733919],
                [1.3424226808222062],
                [1.3617278360175928],
            ],
        ),
        (
            [[2, 1], [4, 2], [8, 3]],
            ["-b", "2"],
            [
                [1.0, 0.0],
                [2.0, 1.0],
                [3.0, 1.5849625007211563],
            ],
        ),
    ],
)
def test_log(
    values: List[List[float]],
    args: List[str],
    expected: List[List[float]],
    tmp_path: Path,
) -> None:
    output = run_command("log", args, values, tmp_path)
    assert output == expected
