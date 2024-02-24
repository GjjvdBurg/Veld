# -*- coding: utf-8 -*-

from veld.console.commands._base import VeldCommand


class PassthroughCommand(VeldCommand):
    def __init__(self):
        super().__init__(
            name="pass",
            title="Pass an input stream through Veld",
            description=(
                "This is a helper command, it is mainly useful to see how "
                "Veld processes a data stream, but can also be used to "
                "flatten a multi-dimensional input stream into a single "
                "column (using the --flatten option)."
            ),
        )

    def handle(self) -> int:
        for values in self._get_stream_processor(keep_text=True):
            print(self.args.separator.join(map(str, values)))
        return 0
