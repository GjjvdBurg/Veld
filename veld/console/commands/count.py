# -*- coding: utf-8 -*-

from veld.console.commands._reducable import ReducableCommand
from veld.core.operators import CountOperator
from veld.stream_processor import BaseStreamProcessor


class CountCommand(ReducableCommand):
    def __init__(self):
        super().__init__(
            operator=CountOperator,
            name="count",
            title="Count the number of values in the data stream",
            description=(
                "This command can be applied to both numeric and non-numeric "
                "data streams."
            ),
        )

    def _get_stream_processor(
        self, keep_text: bool = False
    ) -> BaseStreamProcessor:
        return super()._get_stream_processor(keep_text=True)
