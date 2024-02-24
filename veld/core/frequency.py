# -*- coding: utf-8 -*-

import math

from typing import Counter
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union


class FrequencyTableBuilder:
    def __init__(self, use_percentage: bool, ndigits: int) -> None:
        self._use_percentage = use_percentage
        self._ndigits = ndigits
        self._counter: Optional[Counter[Union[float, str]]] = None

    def get_result(self) -> Optional[List[Tuple[str, Union[float, str]]]]:
        if self._counter is None:
            return None

        count_table: List[Tuple[int, Union[float, str]]] = []
        for key, count in self._counter.items():
            count_table.append((count, key))
        count_table.sort(key=lambda x: (-x[0], str(x[1])))

        output_table: List[Tuple[str, Union[float, str]]] = []
        if self._use_percentage:
            total = self._counter.total()
        for count, key in count_table:
            if self._use_percentage:
                percentage = round(count / total * 100, self._ndigits)
                value = f"{percentage}%"
            else:
                value = str(count)
            output_table.append((value, key))

        return output_table

    def update(self, value: Union[float, str]) -> None:
        if isinstance(value, float) and math.isnan(value):
            return
        if self._counter is None:
            self._counter = Counter()
        self._counter.update([value])
