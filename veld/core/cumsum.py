# -*- coding: utf-8 -*-

from typing import List
from typing import Sequence
from typing import Union


def cumsum(x: Sequence[Union[int, float]]) -> List[Union[int, float]]:
    if not x:
        return []
    y: List[Union[int, float]] = []
    for i, val in enumerate(x):
        prev = 0 if len(y) == 0 else y[-1]
        y.append(prev + val)
    return y
