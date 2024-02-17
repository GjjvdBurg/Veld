# -*- coding: utf-8 -*-

from veld.core.operators import MaxOperator

from ._reducable import ReducableCommand


class MaxCommand(ReducableCommand):
    def __init__(self):
        super().__init__(
            operator=MaxOperator,
            name="max",
            title="Find the maximum of the values in the data stream",
            description=(
                "This command returns the largest value in the data stream. "
                "It can be applied to both numeric and non-numeric values. "
                "For non-numeric values (i.e., strings) the largest "
                "alphabetical value is returned."
            ),
        )
