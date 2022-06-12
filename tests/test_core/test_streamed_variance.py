#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for the StreamedVariance class

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import unittest

from veld.core.streamed_variance import StreamedVariance


class StreamedVarianceTestCase(unittest.TestCase):
    def test_streamed_variance_1(self):
        sv = StreamedVariance()
        for v in range(20):
            sv.update(v)
        self.assertEqual(sv.variance, 35.0)

    def test_streamed_variance_2(self):
        sv = StreamedVariance(population=True)
        for v in range(20):
            sv.update(v)
        self.assertEqual(sv.variance, 33.25)

    def test_streamed_variance_3(self):
        sv = StreamedVariance()
        for v in range(30):
            sv.update(v)
        self.assertEqual(sv.stdev, 8.803408430829505)

    def test_streamed_variance_4(self):
        sv = StreamedVariance(population=True)
        for v in range(10):
            sv.update(v)
        self.assertEqual(sv.stdev, 2.8722813232690143)


if __name__ == "__main__":
    unittest.main()
