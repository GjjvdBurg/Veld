# -*- coding: utf-8 -*-

from typing import List
from typing import Optional

from veld.stream_processor import StreamProcessor

from .base import BaseCommand


class CumSumCommand(BaseCommand):
    def __init__(self):
        super().__init__(
            name="cumsum",
            title="Compute the cumulative sum of the input stream",
        )

    def register(self):
        super().register()

    def handle(self) -> int:
        sp = StreamProcessor(
            path=self.args.file,
            sep=self.args.separator,
            encoding=self.args.encoding,
            flatten=self.args.flatten,
            ignore_invalid=self.args.ignore,
        )
        out_values = None  # type: Optional[List[float]]
        for values in sp:
            if out_values is None:
                out_values = [0] * len(values)

            for i in range(len(values)):
                out_values[i] += values[i]
            print(self.args.separator.join(map(str, out_values)))
        return 0
