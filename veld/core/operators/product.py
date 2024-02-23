# -*- coding: utf-8 -*-

import math

from typing import Optional

from ._base import BaseOperator
from ._container import SingleResultContainerNumeric


class ProductOperator(BaseOperator):
    def __init__(self):
        self._total: Optional[float] = None

    @property
    def result(self) -> Optional[SingleResultContainerNumeric]:
        if self._total is None:
            return None
        return SingleResultContainerNumeric(self._total)

    def update(self, value: float) -> None:
        if math.isnan(value):
            return
        if self._total is None:
            self._total = 1
        self._total *= value
