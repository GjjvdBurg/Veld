# -*- coding: utf-8 -*-

import math

from typing import List
from typing import Optional

from veld.core.operators._base import BaseOperator
from veld.core.operators._container import SingleResultContainer

# NOTE: MedianOperator is not streaming


class MedianOperator(BaseOperator):
    def __init__(self):
        self._values: Optional[List[float]] = None

    @property
    def result(self) -> Optional[SingleResultContainer]:
        if self._values is None:
            return None
        self._values.sort()
        n = len(self._values)
        i = n // 2
        if n % 2 == 1:
            median = self._values[i]
        else:
            median = (self._values[i - 1] + self._values[i]) / 2
        return SingleResultContainer(median)

    def update(self, value: float) -> None:
        if math.isnan(value):
            return
        if self._values is None:
            self._values = []
        self._values.append(value)
