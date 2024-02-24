# -*- coding: utf-8 -*-

from veld.console.commands._reducable import ReducableCommand
from veld.core.operators import SumOperator


class SumCommand(ReducableCommand):
    def __init__(self):
        super().__init__(
            operator=SumOperator,
            name="sum",
            title="Sum the values in the data stream",
        )
