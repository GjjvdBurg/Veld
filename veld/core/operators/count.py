# -*- coding: utf-8 -*-

import math

from typing import Optional, Union

from ._base import BaseOperator
from ._container import SingleResultContainer


class CountOperator(BaseOperator):
    def __init__(self):
        self._count: Optional[int] = None

    @property
    def result(self) -> Optional[SingleResultContainer]:
        if self._count is None:
            return None
        return SingleResultContainer(self._count)

    def update(self, value: Union[float, str]) -> None:
        if isinstance(value, float) and math.isnan(value):
            return None
        self._count = 0 if self._count is None else self._count
        self._count += 1
