# -*- coding: utf-8 -*-

from typing import Optional

from ._base import BaseOperator


class SumOperator(BaseOperator):
    def __init__(self):
        self._total: Optional[float] = None

    @property
    def result(self) -> Optional[float]:
        return self._total

    def update(self, value: float) -> None:
        self._total = 0 if self._total is None else self._total
        self._total += value
