# -*- coding: utf-8 -*-

from typing import List
from typing import Optional

from veld.stream_processor import StreamProcessor

from .base import BaseCommand


class MedianCommand(BaseCommand):
    def __init__(self):
        super().__init__(
            name="median",
            title="Find the median of the values in the data stream",
        )

    def handle(self) -> int:
        all_values = self._consume_stream()
        if all_values is None:
            # no data received
            return 0

        for values in all_values:
            values.sort()

        medians = []
        for values in all_values:
            n = len(values)
            i = n // 2
            if n % 2 == 1:
                median = values[i]
            else:
                median = (values[i - 1] + values[i]) / 2
            medians.append(median)

        print(self.args.separator.join(map(str, medians)))
        return 0