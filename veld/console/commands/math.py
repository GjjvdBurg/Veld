from veld.console.commands._base import VeldCommand
from veld.utils import parse_numeric


class AddCommand(VeldCommand):
    def __init__(self):
        super().__init__(
            name="add", title="Add number to values in the stream"
        )

    def register(self):
        super().register()
        self.add_argument(
            "-v",
            "--value",
            type=parse_numeric,
            help="Number to add",
            required=True,
        )

    def handle(self) -> int:
        for values in self._get_stream_processor():
            outvalues = [val + self.args.value for val in values]
            print(self.args.separator.join(map(str, outvalues)))
        return 0


class SubtractCommand(VeldCommand):
    def __init__(self):
        super().__init__(
            name="subtract", title="Subtract number from values in the stream"
        )

    def register(self):
        super().register()
        self.add_argument(
            "-v",
            "--value",
            type=parse_numeric,
            help="Number to subtract",
            required=True,
        )

    def handle(self) -> int:
        for values in self._get_stream_processor():
            outvalues = [val - self.args.value for val in values]
            print(self.args.separator.join(map(str, outvalues)))
        return 0


class MultiplyCommand(VeldCommand):
    def __init__(self):
        super().__init__(
            name="multiply", title="Multiply values in the stream by number"
        )

    def register(self):
        super().register()
        self.add_argument(
            "-v",
            "--value",
            type=parse_numeric,
            help="Number with which to multiply",
            required=True,
        )

    def handle(self) -> int:
        for values in self._get_stream_processor():
            outvalues = [val * self.args.value for val in values]
            print(self.args.separator.join(map(str, outvalues)))
        return 0


class DivideCommand(VeldCommand):
    def __init__(self):
        super().__init__(
            name="divide", title="Divide values in the stream by a number"
        )

    def register(self):
        super().register()
        self.add_argument(
            "-v",
            "--value",
            type=parse_numeric,
            help="Number by which to divide",
            required=True,
        )

    def handle(self) -> int:
        for values in self._get_stream_processor():
            outvalues = [val / self.args.value for val in values]
            print(self.args.separator.join(map(str, outvalues)))
        return 0


class ModuloCommand(VeldCommand):
    def __init__(self):
        super().__init__(
            name="modulo",  # spelled out to differentiate from mode
            title="Compute the remainder of values in the stream",
        )

    def register(self):
        super().register()
        self.add_argument(
            "-v",
            "--value",
            type=parse_numeric,
            help="The divisor (modulus) of the modulo operation",
            required=True,
        )

    def handle(self) -> int:
        for values in self._get_stream_processor():
            outvalues = [val % self.args.value for val in values]
            print(self.args.separator.join(map(str, outvalues)))
        return 0
