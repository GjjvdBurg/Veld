# -*- coding: utf-8 -*-

import math

from typing import Counter
from typing import Optional
from typing import Union

from veld.core.operators._base import BaseOperator
from veld.core.operators._container import SingleResultContainer


class ModeOperator(BaseOperator):
    def __init__(self):
        self._counter: Optional[Counter[Union[float, str]]] = None

    @property
    def result(self) -> Optional[SingleResultContainer]:
        if self._counter is None:
            return None
        most_common = self._counter.most_common(1)
        most_common_value = most_common[0][1]
        max_keys = [
            k for k, v in self._counter.items() if v == most_common_value
        ]
        return SingleResultContainer(min(max_keys))

    def update(self, value: Union[float, str]) -> None:
        if isinstance(value, float) and math.isnan(value):
            return
        if self._counter is None:
            self._counter = Counter()
        self._counter.update([value])
