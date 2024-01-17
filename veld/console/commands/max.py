# -*- coding: utf-8 -*-

from veld.core.operators import MaxOperator

from ._reducable import ReducableCommand


class MaxCommand(ReducableCommand):
    def __init__(self):
        super().__init__(
            operator=MaxOperator,
            name="max",
            title="Find the maximum of the values in the data stream",
        )
