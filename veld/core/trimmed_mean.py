# -*- coding: utf-8 -*-

import math

from typing import List


def trimmed_mean(x: List[float], keep_percentage: float) -> float:
    if not x:
        return math.nan
    y = sorted(x)
    n_obs = len(y)
    lower = int(n_obs * (1 - keep_percentage / 100) / 2)
    upper = n_obs - lower
    values = y[lower:upper]
    return sum(values) / len(values)
