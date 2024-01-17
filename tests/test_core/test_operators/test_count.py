#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for count operator

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import unittest

from veld.core.operators import CountOperator


class CountOperatorTestCase(unittest.TestCase):
    def test_count_1(self):
        x = [4, 8, 2]
        exp = [1, 2, 3]
        op = CountOperator()
        for v, e in zip(x, exp):
            op.update(v)
            self.assertEqual(op.result, e)

    def test_count_2(self):
        op = CountOperator()
        self.assertIsNone(op.result)


if __name__ == "__main__":
    unittest.main()
