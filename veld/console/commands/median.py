# -*- coding: utf-8 -*-

from veld.console.commands._reducable import ReducableCommand
from veld.core.operators import MedianOperator


class MedianCommand(ReducableCommand):
    def __init__(self):
        super().__init__(
            operator=MedianOperator,
            name="median",
            title="Find the median of the values in the data stream",
        )
