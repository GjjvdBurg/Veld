# -*- coding: utf-8 -*-

from veld.core.operators import ModeOperator

from ._reducable import ReducableCommand


class ModeCommand(ReducableCommand):
    def __init__(self):
        super().__init__(
            operator=ModeOperator,
            name="mode",
            title="Find the mode of the values in the data stream",
            description=(
                "This command finds the modal (most common) value of the data "
                "stream. If there are multiple values with the same count, "
                "the smallest value is returned."
            ),
        )
