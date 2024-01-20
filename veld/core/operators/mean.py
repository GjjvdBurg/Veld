# -*- coding: utf-8 -*-

from typing import Optional

from ._base import BaseOperator


class MeanOperator(BaseOperator):
    def __init__(self):
        self._total: Optional[float] = None
        self._count = 0

    @property
    def result(self) -> Optional[float]:
        if self._total is None:
            return None
        return self._total / self._count

    def update(self, value: float) -> None:
        if self._total is None:
            self._total = 0.0
        self._total += value
        self._count += 1
