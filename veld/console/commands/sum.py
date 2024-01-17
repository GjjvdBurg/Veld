# -*- coding: utf-8 -*-

from veld.core.operators import SumOperator

from ._reducable import ReducableCommand


class SumCommand(ReducableCommand):
    def __init__(self):
        super().__init__(
            operator=SumOperator,
            name="sum",
            title="Sum the values in the data stream",
        )
