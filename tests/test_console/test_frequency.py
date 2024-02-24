#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from tests.test_console.helpers import run_command


@pytest.mark.parametrize(
    ("values", "args", "expected"),
    [
        (
            [
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
            ],
            [],
            [[6, "c"], [5, "a"], [4, "b"], [4, "d"]],
        ),
        (
            [
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
            ],
            ["--percentage", "--ndigits", "3"],
            [
                ["30.0%", "c"],
                ["25.0%", "a"],
                ["25.0%", "b"],
                ["20.0%", "d"],
            ],
        ),
    ],
)
def test_frequency(values, args, expected, tmp_path) -> None:
    assert expected == run_command("frequency", args, values, tmp_path)
