# -*- coding: utf-8 -*-

from typing import List

import numpy as np

from veld.console.commands._base import VeldCommand


class QuantileCommand(VeldCommand):
    def __init__(self):
        super().__init__(
            name="quantile",
            title="Find the given quantile for the data in the stream",
        )

    def register(self) -> None:
        super().register()
        self.add_argument(
            "-q",
            "--quantile",
            help="Quantile to compute",
            type=float,
            required=True,
        )

    def handle(self) -> int:
        columns: List[List[float]] = self._consume_stream()
        if columns is None:
            return 0

        quantiles = [np.quantile(col, self.args.quantile) for col in columns]
        print(self.args.separator.join(map(str, quantiles)))
        return 0
