# -*- coding: utf-8 -*-

from typing import Type

from veld.core.operators._base import BaseOperator
from veld.core.operators._wrapper import OperatorWrapper

from ._base import VeldCommand


class ReducableCommand(VeldCommand):
    def __init__(self, operator: Type[BaseOperator], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._operator = operator

    def register(self):
        super().register()
        self._processing_args_group.add_argument(
            "-r",
            "--reduce",
            help="Apply operator row-wise, reducing rows to a single value",
            action="store_true",
            description=(
                "By default Veld applies operators column-wise, retaining the "
                "dimension of the input values. With the --reduce option the "
                "operation is performed on individual rows (i.e., lines) "
                "instead, so a single value is returned for each line of data "
                "in the input."
            ),
        )

    def handle(self) -> int:
        wrapper = OperatorWrapper(self._operator, reduce=self.args.reduce)
        sep = self.args.separator
        for row in self.default_stream_processor:
            wrapper.update(row)
            if self.args.reduce:
                print(str(wrapper.result))
                wrapper.reset()
        if not self.args.reduce:
            print(sep.join(map(str, wrapper.row_result)))
        return 0
