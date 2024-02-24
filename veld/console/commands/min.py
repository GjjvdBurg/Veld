# -*- coding: utf-8 -*-

from veld.console.commands._reducable import ReducableCommand
from veld.core.operators import MinOperator


class MinCommand(ReducableCommand):
    def __init__(self):
        super().__init__(
            operator=MinOperator,
            name="min",
            title="Find the minimum of the values in the data stream",
            description=(
                "This command finds the smallest value in the data stream. It "
                "can be applied to both numeric and non-numeric values. For "
                "non-numeric values (i.e., strings) the smallest alphabetical "
                "value is returned."
            ),
        )
