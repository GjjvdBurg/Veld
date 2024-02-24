# -*- coding: utf-8 -*-

import math

from typing import Optional

from veld.core.operators._base import BaseOperator
from veld.core.operators._container import SingleResultContainerNumeric


class MeanOperator(BaseOperator):
    def __init__(self):
        self._total: Optional[float] = None
        self._count = 0

    @property
    def result(self) -> Optional[SingleResultContainerNumeric]:
        if self._total is None:
            return None
        return SingleResultContainerNumeric(self._total / self._count)

    def update(self, value: float) -> None:
        if math.isnan(value):
            return
        if self._total is None:
            self._total = 0
        self._total += value
        self._count += 1
