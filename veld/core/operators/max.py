# -*- coding: utf-8 -*-

from typing import Optional

from ._base import BaseOperator


class MaxOperator(BaseOperator):
    def __init__(self):
        self._maximum = None  # type: Optional[float]

    @property
    def result(self) -> Optional[float]:
        return self._maximum

    def update(self, value: float) -> None:
        if self._maximum is None:
            self._maximum = value
        self._maximum = max(self._maximum, value)
