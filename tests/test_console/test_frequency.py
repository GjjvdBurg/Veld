#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from tests.test_console.helpers import run_command

_VALUES = [
    ["a"],
    ["b"],
    ["c"],
    ["a"],
    ["b"],
    ["c"],
    ["a"],
    ["a"],
    ["b"],
    ["c"],
    ["a"],
    ["b"],
    ["c"],
    ["c"],
    ["c"],
    ["d"],
    ["d"],
    ["d"],
    ["d"],
    ["b"],
]


@pytest.mark.parametrize(
    ("values", "args", "expected"),
    [
        (  # counts
            _VALUES,
            [],
            [
                [6, "c"],
                [5, "a"],
                [5, "b"],
                [4, "d"],
            ],
        ),
        (  # percentages
            _VALUES,
            ["--percentage", "--ndigits", "3"],
            [
                ["30.0%", "c"],
                ["25.0%", "a"],
                ["25.0%", "b"],
                ["20.0%", "d"],
            ],
        ),
        (  # reversed, counts
            _VALUES,
            ["--reverse", "--ndigits", "3"],
            [
                ["c", 6],
                ["a", 5],
                ["b", 5],
                ["d", 4],
            ],
        ),
        (  # reversed, percentages
            _VALUES,
            ["--percentage", "--reverse", "--ndigits", "3"],
            [
                ["c", "30.0%"],
                ["a", "25.0%"],
                ["b", "25.0%"],
                ["d", "20.0%"],
            ],
        ),
        (  # ascending counts
            _VALUES,
            ["--ascending"],
            [
                [4, "d"],
                [5, "b"],
                [5, "a"],
                [6, "c"],
            ],
        ),
    ],
)
def test_frequency(values, args, expected, tmp_path) -> None:
    assert expected == run_command("frequency", args, values, tmp_path)
