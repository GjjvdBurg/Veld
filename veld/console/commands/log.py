# -*- coding: utf-8 -*-

import math

from veld.stream_processor import StreamProcessor

from .base import BaseCommand


class LogCommand(BaseCommand):
    def __init__(self):
        super().__init__(
            name="log", title="Compute the logarithm of the input stream"
        )

    def register(self):
        super().register()
        self.add_argument(
            "-b",
            "--base",
            type=float,
            default=math.e,
            help="Base of the logarithm to use",
            description=(
                "By default the natural logarithm is computed. Use this "
                "value to set a different base for the logarithm."
            ),
        )

    def handle(self) -> int:
        sp = StreamProcessor(
            path=self.args.file,
            sep=self.args.separator,
            encoding=self.args.encoding,
            flatten=self.args.flatten,
            ignore_invalid=self.args.ignore,
        )
        for values in sp:
            outvalues = []
            for i in range(len(values)):
                val = values[i]
                outvalues.append(math.log(val, self.args.base))
            print(self.args.separator.join(map(str, outvalues)))
        return 0
