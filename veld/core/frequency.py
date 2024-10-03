# -*- coding: utf-8 -*-

import math

from dataclasses import dataclass

from typing import Counter
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union


@dataclass(frozen=True)
class FrequencyRow:
    key: str
    count: int
    percentage: float


@dataclass(frozen=True)
class FrequencyTable:
    table: List[FrequencyRow]

    def render(
        self,
        use_percentage: bool,
        ndigits: int,
        reverse: bool,
        ascending: bool,
    ) -> str:
        output = []
        for row in self.table:
            value = (
                f"{round(row.percentage, ndigits)}%"
                if use_percentage
                else str(row.count)
            )
            if reverse:
                output.append((row.key, value))
            else:
                output.append((value, row.key))
        if ascending:
            output = list(reversed(output))
        return "\n".join(["\t".join(map(str, row)) for row in output])


class FrequencyTableBuilder:
    def __init__(self) -> None:
        self._counter: Optional[Counter[Union[float, str]]] = None

    def get_table(self) -> Optional[FrequencyTable]:
        if self._counter is None:
            return None

        count_table: List[Tuple[int, Union[float, str]]] = []
        for key, count in self._counter.items():
            count_table.append((count, key))
        count_table.sort(key=lambda x: (-x[0], str(x[1])))

        total = self._counter.total()
        return FrequencyTable(
            table=[
                FrequencyRow(
                    key=str(key),
                    count=count,
                    percentage=count / total * 100.0,
                )
                for count, key in count_table
            ]
        )

    def update(self, value: Union[float, str]) -> None:
        if isinstance(value, float) and math.isnan(value):
            return
        if self._counter is None:
            self._counter = Counter()
        self._counter.update([value])
