#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Unit tests for mean operator

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import unittest

from veld.core.operators import MeanOperator


class MeanOperatorTestCase(unittest.TestCase):
    def test_mean_1(self):
        values = [1, 5, 9, 13]
        exp = [1, 3, 5, 7]
        op = MeanOperator()
        for v, e in zip(values, exp):
            op.update(v)
            self.assertEqual(op.result, e)

    def test_mean_2(self):
        op = MeanOperator()
        self.assertIsNone(op.result)
