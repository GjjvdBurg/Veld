#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for max operator

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import unittest

from veld.core.operators import MaxOperator


class MaxOperatorTestCase(unittest.TestCase):
    def test_max_1(self):
        x = [1, 2, 1]
        exp = [1, 2, 2]
        op = MaxOperator()
        for v, e in zip(x, exp):
            op.update(v)
            self.assertEqual(op.result, e)

    def test_max_2(self):
        op = MaxOperator()
        self.assertIsNone(op.result)


if __name__ == "__main__":
    unittest.main()
