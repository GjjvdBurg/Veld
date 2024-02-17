# -*- coding: utf-8 -*-

from veld.core.operators import SummaryOperator

from ._reducable import ReducableCommand

from veld.stream_processor import BaseStreamProcessor

class SummaryCommand(ReducableCommand):
    def __init__(self) -> None:
        super().__init__(
            operator=SummaryOperator,
            name="summary",
            title="Print a summary with commonly-used statistics",
        )

    def _get_stream_processor(
        self, keep_text: bool = False
    ) -> BaseStreamProcessor:
        return super()._get_stream_processor(keep_text=True)
