# -*- coding: utf-8 -*-

import math

from typing import Optional, Union

from ._base import BaseOperator
from ._container import SummaryResultContainer
from .count import CountOperator
from .max import MaxOperator
from .min import MinOperator
from .mode import ModeOperator
from .sum import SumOperator
from .mean import MeanOperator


class SummaryOperator(BaseOperator):
    def __init__(self) -> None:
        self._op_count = CountOperator()
        self._op_mean = MeanOperator()
        self._op_max = MaxOperator()
        self._op_min = MinOperator()
        self._op_mode = ModeOperator()
        self._op_sum = SumOperator()

    @property
    def result(self) -> Optional[SummaryResultContainer]:
        if self._op_count.result is None:
            return None

        # If any of these fail it's an error
        assert self._op_count.result is not None
        assert self._op_max.result is not None
        assert self._op_min.result is not None
        assert self._op_mode.result is not None

        return SummaryResultContainer(
            count=self._op_count.result.value,
            maximum=self._op_max.result.value,
            minimum=self._op_min.result.value,
            mean=(
                self._op_mean.result.value
                if self._op_mean.result is not None
                else None
            ),
            mode=self._op_mode.result.value,
            total=(
                self._op_sum.result.value
                if self._op_sum.result is not None
                else None
            ),
        )

    def update(self, value: Union[float, str]) -> None:
        # these operators can handle non-float inputs
        self._op_count.update(value)
        self._op_min.update(value)
        self._op_max.update(value)
        self._op_mode.update(value)

        # these can't
        if isinstance(value, str):
            # TODO: Should we handle this differently? Mark them disabled as
            # soon as the first non-numeric argument is given and then have
            # them disabled in the UI?
            return
        self._op_mean.update(value)
        self._op_sum.update(value)
