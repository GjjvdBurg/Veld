#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for cumsum function

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import unittest

from typing import List

from veld.core.cumsum import cumsum


class CumSumTestCase(unittest.TestCase):
    def test_cumsum_1(self):
        x = [1, 2, 3]
        exp = [1, 3, 6]
        out = cumsum(x)
        self.assertEqual(out, exp)

    def test_cumsum_2(self):
        x: List[int] = []
        exp: List[int] = []
        out = cumsum(x)
        self.assertEqual(out, exp)


if __name__ == "__main__":
    unittest.main()
