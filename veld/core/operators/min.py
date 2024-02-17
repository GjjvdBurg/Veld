# -*- coding: utf-8 -*-

from typing import Optional

from ._base import BaseOperator
from ._container import SingleResultContainer


class MinOperator(BaseOperator):
    def __init__(self):
        self._minimum: Optional[float] = None

    @property
    def result(self) -> Optional[SingleResultContainer]:
        if self._minimum is None:
            return None
        return SingleResultContainer(self._minimum)

    def update(self, value: float) -> None:
        if self._minimum is None:
            self._minimum = value
        self._minimum = min(self._minimum, value)
