# -*- coding: utf-8 -*-

from typing import Optional

from ._base import BaseOperator


class MinOperator(BaseOperator):
    def __init__(self):
        self._minimum = None  # type: Optional[float]

    @property
    def result(self) -> Optional[float]:
        return self._minimum

    def update(self, value: float) -> None:
        if self._minimum is None:
            self._minimum = value
        self._minimum = min(self._minimum, value)
