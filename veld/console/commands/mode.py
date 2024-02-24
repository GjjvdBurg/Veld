# -*- coding: utf-8 -*-

from veld.console.commands._reducable import ReducableCommand
from veld.core.operators import ModeOperator
from veld.stream_processor import BaseStreamProcessor


class ModeCommand(ReducableCommand):
    def __init__(self):
        super().__init__(
            operator=ModeOperator,
            name="mode",
            title="Find the mode of the values in the data stream",
            description=(
                "This command finds the modal (most common) value of the data "
                "stream. If there are multiple values with the same count, "
                "the smallest value is returned.\n\n"
                "This command can be applied to both numeric and non-numeric "
                "data streams."
            ),
        )

    def _get_stream_processor(
        self, keep_text: bool = False
    ) -> BaseStreamProcessor:
        return super()._get_stream_processor(keep_text=True)
