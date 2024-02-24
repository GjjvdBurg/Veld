# -*- coding: utf-8 -*-

from typing import Any
from typing import List
from typing import Optional
from typing import Type

from veld.console.commands._base import VeldCommand
from veld.core.operators._base import BaseOperator
from veld.core.operators._container import BaseResultContainer
from veld.core.operators._container import SingleResultContainer
from veld.core.operators._container import SummaryResultContainer
from veld.core.operators._wrapper import OperatorWrapper


class ReducableCommand(VeldCommand):
    def __init__(self, operator: Type[BaseOperator], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._operator = operator
        self._printed_header = False  # TODO: refactor

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
        for idx, row in enumerate(self._get_stream_processor()):
            wrapper.update(row)
            if self.args.reduce:
                if wrapper.result is None:
                    continue
                self._print_row_result(idx, wrapper.result)
                wrapper.reset()
        if not self.args.reduce:
            self._print_end_result(wrapper.row_result)
        return 0

    # TODO: testing
    def _print_row_result(
        self, index: int, container: BaseResultContainer
    ) -> None:
        if isinstance(container, SingleResultContainer):
            return print(str(container.value))
        if not isinstance(container, SummaryResultContainer):
            raise ValueError(f"Unhandled container type: {type(container)}")
        sep = self.args.separator
        if not self._printed_header:
            print(
                sep.join(
                    [
                        "Row",
                        "Count",
                        "Minimum",
                        "Maximum",
                        "Mean",
                        "Mode",
                        "Sum",
                    ]
                )
            )
            self._printed_header = True
        print(
            sep.join(
                map(
                    str,
                    [
                        index,
                        container.count,
                        container.minimum,
                        container.maximum,
                        "-" if container.mean is None else container.mean,
                        container.mode,
                        "-" if container.total is None else container.total,
                    ],
                )
            )
        )

    def _print_end_result(
        self, containers: List[Optional[BaseResultContainer]]
    ) -> None:
        sep = self.args.separator
        if all(
            isinstance(container, SingleResultContainer)
            for container in containers
        ):
            row = []
            for container in containers:
                assert isinstance(container, SingleResultContainer)
                row.append("" if container is None else str(container.value))
            return print(sep.join(row))

        table: List[List[Any]] = [
            [
                "Count",
                "Minimum",
                "Maximum",
                "Mean",
                "Mode",
                "Sum",
            ],
        ]
        for container in containers:
            assert isinstance(container, SummaryResultContainer)
            table.append(
                [
                    container.count,
                    container.minimum,
                    container.maximum,
                    "-" if container.mean is None else container.mean,
                    container.mode,
                    "-" if container.total is None else container.total,
                ]
            )

        transposed = list(map(list, zip(*table)))
        print("\n".join([sep.join(map(str, row)) for row in transposed]))
