# -*- coding: utf-8 -*-

import math

from typing import Optional
from typing import Union

from veld.core.operators._base import BaseOperator
from veld.core.operators._container import SingleResultContainer


class MinOperator(BaseOperator):
    def __init__(self):
        self._minimum: Optional[Union[float, str]] = None

    @property
    def result(self) -> Optional[SingleResultContainer]:
        if self._minimum is None:
            return None
        return SingleResultContainer(self._minimum)

    def update(self, value: Union[float, str]) -> None:
        if isinstance(value, float) and math.isnan(value):
            return
        if self._minimum is None:
            self._minimum = value
        self._minimum = min(self._minimum, value)
