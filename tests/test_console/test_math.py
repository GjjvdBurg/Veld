#!/usr/bin/env python

"""Unit tests for math commands

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
        ([[1], [2], [3]], ["-v", "1"], [[0], [1], [2]]),
        (
            [[1, 0], [2, 1], [3, 2]],
            ["-v", "1.5"],
            [[-0.5, -1.5], [0.5, -0.5], [1.5, 0.5]],
        ),
    ],
)
def test_subtract(
    values: List[List[float]],
    args: List[str],
    expected: List[List[float]],
    tmp_path: Path,
) -> None:
    output = run_command("subtract", args, values, tmp_path)
    assert output == expected


@pytest.mark.parametrize(
    ("values", "args", "expected"),
    [
        ([[1], [2], [3]], ["-v", "1"], [[2], [3], [4]]),
        (
            [[1, 0], [2, 1], [3, 2]],
            ["-v", "1.5"],
            [[2.5, 1.5], [3.5, 2.5], [4.5, 3.5]],
        ),
    ],
)
def test_add(
    values: List[List[float]],
    args: List[str],
    expected: List[List[float]],
    tmp_path: Path,
) -> None:
    output = run_command("add", args, values, tmp_path)
    assert output == expected


@pytest.mark.parametrize(
    ("values", "args", "expected"),
    [
        ([[1], [2], [3]], ["-v", "2"], [[2], [4], [6]]),
        (
            [[1, 0], [2, 1], [3, 2]],
            ["-v", "1.5"],
            [[1.5, 0], [3.0, 1.5], [4.5, 3.0]],
        ),
    ],
)
def test_multiply(
    values: List[List[float]],
    args: List[str],
    expected: List[List[float]],
    tmp_path: Path,
) -> None:
    output = run_command("multiply", args, values, tmp_path)
    assert output == expected


@pytest.mark.parametrize(
    ("values", "args", "expected"),
    [
        ([[1], [2], [3]], ["-v", "2"], [[0.5], [1], [1.5]]),
        (
            [[1, 0], [2, 1], [3, 2]],
            ["-v", "1.5"],
            [[2 / 3, 0], [2 / 1.5, 1 / 1.5], [3 / 1.5, 2 / 1.5]],
        ),
    ],
)
def test_divide(
    values: List[List[float]],
    args: List[str],
    expected: List[List[float]],
    tmp_path: Path,
) -> None:
    output = run_command("divide", args, values, tmp_path)
    assert output == expected


@pytest.mark.parametrize(
    ("values", "args", "expected"),
    [
        ([[2], [3], [4]], ["-v", "2"], [[0], [1], [0]]),
        ([[5, 0], [2, 1], [3, 2]], ["-v", "3"], [[2, 0], [2, 1], [0, 2]]),
    ],
)
def test_modulo(
    values: List[List[float]],
    args: List[str],
    expected: List[List[float]],
    tmp_path: Path,
) -> None:
    output = run_command("modulo", args, values, tmp_path)
    assert output == expected
