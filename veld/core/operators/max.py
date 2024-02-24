# -*- coding: utf-8 -*-

import math

from typing import Optional
from typing import Union

from veld.core.operators._base import BaseOperator
from veld.core.operators._container import SingleResultContainer


class MaxOperator(BaseOperator):
    def __init__(self):
        self._maximum: Optional[Union[float, str]] = None

    @property
    def result(self) -> Optional[SingleResultContainer]:
        if self._maximum is None:
            return None
        return SingleResultContainer(self._maximum)

    def update(self, value: Union[float, str]) -> None:
        if isinstance(value, float) and math.isnan(value):
            return
        if self._maximum is None:
            self._maximum = value
        self._maximum = max(self._maximum, value)
