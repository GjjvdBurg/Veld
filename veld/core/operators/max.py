# -*- coding: utf-8 -*-

from typing import Optional

from ._base import BaseOperator
from ._container import SingleResultContainer


class MaxOperator(BaseOperator):
    def __init__(self):
        self._maximum: Optional[float] = None

    @property
    def result(self) -> Optional[SingleResultContainer]:
        if self._maximum is None:
            return None
        return SingleResultContainer(self._maximum)

    def update(self, value: float) -> None:
        if self._maximum is None:
            self._maximum = value
        self._maximum = max(self._maximum, value)
