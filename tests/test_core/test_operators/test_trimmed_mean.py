"""Unit tests for trimmed mean operator

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import math
import random
import unittest

from veld.core.trimmed_mean import trimmed_mean


class TrimmedMeanTestCase(unittest.TestCase):
    def test_trimmed_mean_1(self):
        a = [random.random() for _ in range(40)]
        values = [-123, -456, *a, 233, 781]
        # 44 observations, 5% = 0.44 * 5 = 2.2 obs, so all outliers removed
        self.assertAlmostEqual(trimmed_mean(values, 90), sum(a) / len(a))
        self.assertAlmostEqual(
            trimmed_mean(values, 100), sum(values) / len(values)
        )
        self.assertTrue(math.isnan(trimmed_mean([], 10)))
