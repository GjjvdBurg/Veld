# -*- coding: utf-8 -*-

import math

from typing import List
from typing import Optional

from veld.stream_processor import StreamProcessor

from .base import BaseCommand


class ModeCounter:
    """Version of collections.Counter that returns the minimum mode"""

    def __init__(self):
        self._counter = {}

    def update(self, value: float):
        if not value in self._counter:
            self._counter[value] = 0
        self._counter[value] = self._counter[value] + 1

    def most_common_value(self) -> float:
        max_value = max(self._counter.values())
        max_keys = [k for k, v in self._counter.items() if v == max_value]
        return min(max_keys)


class ModeCommand(BaseCommand):
    def __init__(self):
        super().__init__(
            name="mode",
            title="Find the mode of the values in the data stream",
            description=(
                "This command finds the modal (most common) value of the data "
                "stream. If there are multiple values with the same count, "
                "the smallest value is returned."
            ),
        )

    def handle(self) -> int:
        sp = StreamProcessor(
            path=self.args.file,
            sep=self.args.separator,
            encoding=self.args.encoding,
            flatten=self.args.flatten,
            ignore_invalid=self.args.ignore,
        )

        counters = None  # type: Optional[List[ModeCounter]]
        for values in sp:
            if counters is None:
                counters = [ModeCounter() for _ in range(len(values))]

            for i in range(len(values)):
                val = values[i]
                if math.isnan(val):
                    continue

                counters[i].update(val)

        counters = [] if counters is None else counters
        most_common = [c.most_common_value() for c in counters]
        print(self.args.separator.join(map(str, most_common)))
        return 0
