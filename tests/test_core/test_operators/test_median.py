#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for median operator

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import unittest

from veld.core.operators import MedianOperator
from veld.core.operators import SingleResultContainer


class MedianOperatorTestCase(unittest.TestCase):
    def test_median_1(self):
        x = [1, 6, 5]
        exp = 5
        op = MedianOperator()
        for v in x:
            op.update(v)
        self.assertEqual(op.result, SingleResultContainer(exp))

    def test_median_2(self):
        x = [1, 5, 6, 8]
        exps = [1, 3, 5, 5.5]
        op = MedianOperator()
        for v, e in zip(x, exps):
            op.update(v)
            self.assertEqual(op.result, SingleResultContainer(e))

    def test_median_3(self):
        op = MedianOperator()
        self.assertIsNone(op.result)


if __name__ == "__main__":
    unittest.main()
