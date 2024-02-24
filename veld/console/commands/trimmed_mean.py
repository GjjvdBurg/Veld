# -*- coding: utf-8 -*-

from typing import List

from veld.console.commands._base import VeldCommand
from veld.core.trimmed_mean import trimmed_mean


class TrimmedMeanCommand(VeldCommand):
    def __init__(self):
        super().__init__(
            name="trimmed-mean",
            title="Compute the trimmed mean for data in the stream",
        )

    def register(self) -> None:
        super().register()
        self.add_argument(
            "-k",
            "--keep",
            help="Percentage to keep (default: 95)",
            type=float,
            default=95,
        )

    def handle(self) -> int:
        columns: List[List[float]] = self._consume_stream()
        if columns is None:
            return 0

        tmeans = [
            trimmed_mean(col, keep_percentage=self.args.keep)
            for col in columns
        ]
        print(self.args.separator.join(map(str, tmeans)))
        return 0
