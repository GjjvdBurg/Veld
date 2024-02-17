#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for min operator

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import unittest

from veld.core.operators import MinOperator
from veld.core.operators import SingleResultContainer


class MinOperatorTestCase(unittest.TestCase):
    def test_min_1(self):
        x = [1, 2, -3]
        exp = [1, 1, -3]
        op = MinOperator()
        for v, e in zip(x, exp):
            op.update(v)
            self.assertEqual(op.result, SingleResultContainer(e))

    def test_min_2(self):
        x = ["a", "b", "c", "a", "b", "c", "a", "a", "b", "c", "a", "b"]
        op = MinOperator()
        for v in x:
            op.update(v)
        self.assertEqual(op.result, SingleResultContainer("a"))

    def test_min_3(self):
        op = MinOperator()
        self.assertIsNone(op.result)


if __name__ == "__main__":
    unittest.main()
