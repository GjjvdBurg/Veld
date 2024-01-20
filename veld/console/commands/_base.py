# -*- coding: utf-8 -*-

"""Base command for all Veld commands

"""

from typing import List
from typing import Optional

from wilderness import Command

from veld.stream_processor import StreamProcessor


class VeldCommand(Command):
    def register(self):
        self.add_argument(
            "file",
            help="File to read from (otherwise stdin)",
            nargs="?",
            description=(
                "Veld is primarily designed for processing input streams, "
                "but it can also be applied on a file of data, which can "
                "be supplied with this argument. By default Veld will read "
                "the input data from stdin."
            ),
        )
        group = self.add_argument_group(title="processing options")
        group.add_argument(
            "-e",
            "--encoding",
            help="Encoding of the input stream",
            default="utf-8",
            description=("Specify the encoding of the input stream."),
        )
        group.add_argument(
            "-f",
            "--flatten",
            help="Apply operation on flattened input",
            action="store_true",
            description=(
                "With multidimensional input (more than one value per line) "
                "the operation is normally conducted on each dimension "
                "independently. With the --flatten option, the input is "
                "flattened line-wise (RowMajor order) and the operation "
                "is conducted on the resulting one-dimensional stream."
            ),
        )
        group.add_argument(
            "-i",
            "--ignore",
            help="Ignore non-numeric values in the input stream",
            action="store_true",
        )
        group.add_argument(
            "-s",
            "--separator",
            help="Separator for values in the stream",
            description=(
                "Some of the Veld commands have support for "
                "multidimensional input data. The values on each line "
                "of the input stream are expected to be separated by this "
                "separator. By default, the tab character will be used as "
                "a separator."
            ),
            default="\t",
        )
        self._processing_args_group = group

    def _get_stream_processor(
        self, ignore_invalid: bool = False
    ) -> StreamProcessor:
        sp = StreamProcessor(
            path=self.args.file,
            sep=self.args.separator,
            encoding=self.args.encoding,
            flatten=self.args.flatten,
            ignore_invalid=ignore_invalid or self.args.ignore,
        )
        return sp

    def _consume_stream(
        self, ignore_invalid: bool = False
    ) -> Optional[List[List[float]]]:
        """Read the data stream into memory as a list of columns"""
        columns: Optional[List[List[float]]] = None
        for row in self._get_stream_processor(ignore_invalid=ignore_invalid):
            for i, value in enumerate(row):
                if columns is None:
                    columns = []
                    for j in range(len(row)):
                        columns.append([])
                columns[i].append(value)
        return columns
