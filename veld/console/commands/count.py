# -*- coding: utf-8 -*-

from veld.core.operators import CountOperator

from ._reducable import ReducableCommand


class CountCommand(ReducableCommand):
    def __init__(self):
        super().__init__(
            operator=CountOperator,
            name="count",
            title="Count the number of values in the data stream",
        )
