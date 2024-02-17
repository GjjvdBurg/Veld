#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for sum operator

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import unittest

from veld.core.operators import SumOperator
from veld.core.operators import SingleResultContainer


class SumOperatorTestCase(unittest.TestCase):
    def test_sum_1(self):
        x = [1, 2, 3]
        exp = [1, 3, 6]
        op = SumOperator()
        for v, e in zip(x, exp):
            op.update(v)
            self.assertEqual(op.result, SingleResultContainer(e))

    def test_sum_2(self):
        op = SumOperator()
        self.assertIsNone(op.result)


if __name__ == "__main__":
    unittest.main()
