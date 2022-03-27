# -*- coding: utf-8 -*-

import math

from typing import List
from typing import Optional

from veld.stream_processor import StreamProcessor

from .base import BaseCommand


class MinCommand(BaseCommand):
    def __init__(self):
        super().__init__(
            name="min",
            title="Find the minimum of the values in the data stream",
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
        mins = None  # type: Optional[List[float]]
        for values in sp:
            if mins is None:
                mins = [float("inf")] * len(values)

            for i in range(len(values)):
                val = values[i]
                if math.isnan(val):
                    continue
                mins[i] = min(mins[i], val)

        mins = [] if mins is None else mins
        print(" ".join(map(str, mins)))
        return 0
