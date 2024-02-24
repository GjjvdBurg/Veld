# -*- coding: utf-8 -*-

from veld.console.commands._reducable import ReducableCommand
from veld.core.operators import SummaryOperator
from veld.stream_processor import BaseStreamProcessor


class SummaryCommand(ReducableCommand):
    def __init__(self) -> None:
        super().__init__(
            operator=SummaryOperator,
            name="summary",
            title="Print a summary with commonly-used statistics",
            description=(
                "The summary command prints an overview of summary statistics "
                "for the data stream. For multi-dimensional input (i.e., "
                "multiple columns), the summary is printed for each column "
                "individually. If the --reduce option is set, the summary is "
                "printed for each row in the input stream.\n\n"
                "This command can be applied to non-numeric data streams, but "
                "some statistics will be undefined (e.g., sum, mean, etc)."
            ),
        )

    def _get_stream_processor(
        self, keep_text: bool = False
    ) -> BaseStreamProcessor:
        return super()._get_stream_processor(keep_text=True)
