# -*- coding: utf-8 -*-

from veld.console.commands._reducable import ReducableCommand
from veld.core.operators import MeanOperator


class MeanCommand(ReducableCommand):
    def __init__(self):
        super().__init__(
            operator=MeanOperator,
            name="mean",
            title="Find the mean (average) of the values in the data stream",
            extra_sections={
                "Examples": (
                    # TODO: Make this a test case for groffify in Wilderness
                    "Below are some examples of using the mean command."
                    "\n\n"
                    "1. Taking the mean of a univariate data stream:\n"
                    "$ seq 12 | veld mean\n"
                    "6.5\n\n"
                    "2. Mean of a multidimensional data stream:\n"
                    "$ paste <(seq 5) <(seq 5 9) | veld mean\n"
                    "3.0\t7.0\n\n"
                    "3. Multivariate data stream flattened into a univariate one:\n"
                    "$ paste <(seq 5) <(seq 5 9) | veld mean --flatten\n"
                    "5.0\n\n"
                    "4. Multivariate data stream averaged row-wise:\n"
                    "$ paste <(seq 5) <(seq 5 9) | veld mean --reduce\n"
                    "\n\n"
                    "3.0"
                    "\n\n"
                    "4.0"
                    "\n\n"
                    "5.0"
                    "\n\n"
                    "6.0"
                    "\n\n"
                    "7.0"
                    "\n\n"
                )
            },
        )
