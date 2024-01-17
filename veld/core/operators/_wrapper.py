# -*- coding: utf-8 -*-

import math

from typing import List
from typing import Optional
from typing import Type

from ._base import BaseOperator


class OperatorWrapper:
    def __init__(
        self, operator_class: Type[BaseOperator], reduce: bool = False
    ):
        self._operator_class = operator_class
        self._reduce = reduce
        self._single = None  # type: Optional[BaseOperator]
        self._multi = None  # type: Optional[List[BaseOperator]]

    @property
    def row_result(self) -> List[Optional[float]]:
        assert self._multi is not None
        return [op.result for op in self._multi]

    @property
    def result(self) -> Optional[float]:
        assert self._single is not None
        return self._single.result

    def reset(self) -> None:
        self._single = None
        self._multi = None

    def update_single(self, values: List[float]) -> None:
        if self._single is None:
            self._single = self._operator_class()
        for val in values:
            if math.isnan(val):
                continue
            self._single.update(val)

    def update_multi(self, values: List[float]) -> None:
        if self._multi is None:
            self._multi = [self._operator_class() for val in values]
        for op, val in zip(self._multi, values):
            if math.isnan(val):
                continue
            op.update(val)

    def update(self, values: List[float]) -> None:
        if self._reduce:
            return self.update_single(values)
        return self.update_multi(values)
