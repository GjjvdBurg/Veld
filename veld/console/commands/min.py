# -*- coding: utf-8 -*-

from veld.core.operators import MinOperator

from ._reducable import ReducableCommand


class MinCommand(ReducableCommand):
    def __init__(self):
        super().__init__(
            operator=MinOperator,
            name="min",
            title="Find the minimum of the values in the data stream",
        )
