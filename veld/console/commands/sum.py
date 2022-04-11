# -*- coding: utf-8 -*-

import math

from typing import List
from typing import Optional

from veld.stream_processor import StreamProcessor

from .base import BaseCommand


class SumCommand(BaseCommand):
    def __init__(self):
        super().__init__(
            name="sum",
            title="Sum the values in the data stream",
        )

    def handle(self) -> int:
        sp = StreamProcessor(
            path=self.args.file,
            sep=self.args.separator,
            encoding=self.args.encoding,
            flatten=self.args.flatten,
            ignore_invalid=self.args.ignore,
        )
        totals = None  # type: Optional[List[float]]
        for values in sp:
            if totals is None:
                totals = [0] * len(values)

            for i in range(len(values)):
                val = values[i]
                if math.isnan(val):
                    continue
                totals[i] += val

        totals = [] if totals is None else totals
        print(self.args.separator.join(map(str, totals)))
        return 0
