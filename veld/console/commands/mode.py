# -*- coding: utf-8 -*-

from veld.core.operators import ModeOperator

from ._reducable import ReducableCommand
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
                "the smallest value is returned."
            ),
        )

    def _get_stream_processor(
        self, keep_text: bool = False
    ) -> BaseStreamProcessor:
        return super()._get_stream_processor(keep_text=True)
