# -*- coding: utf-8 -*-

from typing import List
from typing import Optional

from ._base import BaseOperator


class MedianOperator(BaseOperator):
    def __init__(self):
        self._values: Optional[List[float]] = None

    @property
    def result(self) -> Optional[float]:
        if self._values is None:
            return None
        self._values.sort()
        n = len(self._values)
        i = n // 2
        if n % 2 == 1:
            median = self._values[i]
        else:
            median = (self._values[i - 1] + self._values[i]) / 2
        return median

    def update(self, value: float) -> None:
        if self._values is None:
            self._values = []
        self._values.append(value)
