# -*- coding: utf-8 -*-

from typing import List
from typing import Optional
from typing import Type

from veld.core.operators._base import BaseOperator
from veld.core.operators._container import BaseResultContainer


class OperatorWrapper:
    def __init__(
        self, operator_class: Type[BaseOperator], reduce: bool = False
    ):
        self._operator_class = operator_class
        self._reduce = reduce
        self._single: Optional[BaseOperator] = None
        self._multi: Optional[List[BaseOperator]] = None

    @property
    def row_result(self) -> List[Optional[BaseResultContainer]]:
        assert self._multi is not None
        return [op.result for op in self._multi]

    @property
    def result(self) -> Optional[BaseResultContainer]:
        assert self._single is not None
        return self._single.result

    def reset(self) -> None:
        self._single = None
        self._multi = None

    def update_single(self, values: List[float]) -> None:
        if self._single is None:
            self._single = self._operator_class()
        for val in values:
            self._single.update(val)

    def update_multi(self, values: List[float]) -> None:
        if self._multi is None:
            self._multi = [self._operator_class() for val in values]
        for op, val in zip(self._multi, values):
            op.update(val)

    def update(self, values: List[float]) -> None:
        if self._reduce:
            return self.update_single(values)
        return self.update_multi(values)
