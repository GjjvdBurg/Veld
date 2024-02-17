# -*- coding: utf-8 -*-

from typing import Dict
from typing import Optional

from ._base import BaseOperator
from ._container import SingleResultContainer


class ModeOperator(BaseOperator):
    def __init__(self):
        self._counter: Optional[Dict[float, int]] = None

    @property
    def result(self) -> Optional[SingleResultContainer]:
        if self._counter is None:
            return None
        max_value = max(self._counter.values())
        max_keys = [k for k, v in self._counter.items() if v == max_value]
        return SingleResultContainer(min(max_keys))

    def update(self, value: float) -> None:
        if self._counter is None:
            self._counter = {}
        if value not in self._counter:
            self._counter[value] = 0
        self._counter[value] += 1
