# -*- coding: utf-8 -*-

from typing import List
from typing import Optional

from veld.stream_processor import StreamProcessor

from .base import BaseCommand


class VarianceCommand(BaseCommand):
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
        sp = StreamProcessor(
            path=self.args.file,
            sep=self.args.separator,
            encoding=self.args.encoding,
            flatten=self.args.flatten,
            ignore_invalid=self.args.ignore,
        )

        counts = None  # type: Optional[List[int]]
        means = []  # type: List[float]
        sqdevs = []  # type: List[float]

        for values in sp:
            if counts is None:
                counts = [0] * len(values)
                means = [0] * len(values)
                sqdevs = [0] * len(values)

            # This is a memory efficient approach to compute the variance, by
            # only keeping track of counts, means, and squared deviations. See
            # also: https://gertjanvandenburg.com/blog/thompson_sampling/
            for i in range(len(values)):
                N_prev = counts[i]
                mean_prev = means[i]
                sqdev_prev = sqdevs[i]

                value = values[i]

                N = N_prev + 1
                mean = mean_prev + 1 / (N_prev + 1) * (value - mean_prev)
                sqdev = (
                    sqdev_prev
                    + value * value
                    + N_prev * mean_prev * mean_prev
                    - N * mean * mean
                )

                counts[i] = N
                means[i] = mean
                sqdevs[i] = sqdev

        safediv = lambda a, b: float("nan") if b == 0 else a / b

        counts = [] if counts is None else counts
        if self.args.population:
            out = [safediv(sqdevs[i], counts[i]) for i in range(len(counts))]
        else:
            out = [
                safediv(sqdevs[i], counts[i] - 1) for i in range(len(counts))
            ]
        print(self.args.separator.join(map(str, out)))
        return 0
