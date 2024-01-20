# -*- coding: utf-8 -*-

from typing import List
from typing import Optional

from veld.core.streamed_variance import StreamedVariance

from ._base import VeldCommand


class VarianceCommand(VeldCommand):
    def __init__(self):
        super().__init__(
            name="variance",
            title="Compute the variance of the input stream",
            extra_sections={
                "NOTES": (
                    "1. https://en.wikipedia.org/wiki/Variance#Unbiased_sample_variance"
                )
            },
        )

    def register(self):
        super().register()
        self.add_argument(
            "-p",
            "--population",
            help="Compute the population variance instead of the sample variance",
            description=(
                "By default the Veld variance command computes an unbiased "
                "estimator of the sample variance using Bessel's correction "
                "[1]. If the data stream constitutes the entirety of a "
                "finite population, then you can use this flag to compute "
                "the population variance."
            ),
            action="store_true",
        )

    def handle(self) -> int:
        svs: Optional[List[StreamedVariance]] = None

        for values in self.default_stream_processor:
            if svs is None:
                svs = [
                    StreamedVariance(population=self.args.population)
                    for _ in range(len(values))
                ]

            for i in range(len(values)):
                svs[i].update(values[i])

        svs = [] if svs is None else svs
        variances = [sv.variance for sv in svs]
        print(self.args.separator.join(map(str, variances)))
        return 0
