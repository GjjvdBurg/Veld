# -*- coding: utf-8 -*-

from veld.core.operators import SummaryOperator

from ._reducable import ReducableCommand


class SummaryCommand(ReducableCommand):
    def __init__(self) -> None:
        super().__init__(
            operator=SummaryOperator,
            name="summary",
            title="Print a summary with commonly-used statistics",
        )
