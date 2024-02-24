# -*- coding: utf-8 -*-

from veld.console.commands._base import VeldCommand
from veld.core.frequency import FrequencyTableBuilder
from veld.exceptions import EmptyStreamError
from veld.exceptions import InvalidInputError
from veld.stream_processor import BaseStreamProcessor


class FrequencyCommand(VeldCommand):
    def __init__(self):
        super().__init__(
            name="frequency",
            title="Print a frequency table of unique values in the stream",
            description=(
                "This command can be applied to both numeric and non-numeric "
                "data streams.\n\n"
                "This is equivalent to `sort | uniq -c | sort -k 1nr,2`, but "
                "with optional support for showing percentages."
            ),
        )

    def register(self) -> None:
        super().register()
        self.add_argument(
            "-p",
            "--percentage",
            action="store_true",
            help="Show percentages instead of counts",
        )
        self.add_argument(
            "-n",
            "--ndigits",
            type=int,
            default=2,
            help="Rounding precision for the percentages",
        )

    def _get_stream_processor(
        self, keep_text: bool = False
    ) -> BaseStreamProcessor:
        return super()._get_stream_processor(keep_text=True)

    def handle(self) -> int:
        builder = FrequencyTableBuilder(
            self.args.percentage, ndigits=self.args.ndigits
        )
        for values in self._get_stream_processor(keep_text=True):
            if len(values) > 1:
                raise InvalidInputError(
                    f"The {self.name} command can only be used for "
                    "one-dimensional data streams"
                )
            value = values[0]
            builder.update(value)
        result = builder.get_result()
        if result is None:
            raise EmptyStreamError()
        print("\n".join(["\t".join(map(str, row)) for row in result]))
        return 0
