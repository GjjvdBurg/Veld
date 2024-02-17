"""Helpers for running command tests"""

from pathlib import Path

from typing import Any
from typing import List, Union

from wilderness import Tester

from veld.console import build_application
from veld.utils import parse_numeric


def maybe_parse(x: str) -> Union[str, float]:
    try:
        return parse_numeric(x)
    except ValueError:
        pass
    return x


def run_command(
    command: str, args: List[str], values: List[List[Any]], tmp_path: Path
) -> List[List[Any]]:
    filename = tmp_path / "file.txt"
    with open(filename, "w") as fileobj:
        fileobj.write("\n".join(["\t".join(map(str, row)) for row in values]))

    app = build_application()
    tester = Tester(app)
    tester.test_command(command, [*args, str(filename)])

    stdout = tester.get_stdout()
    assert stdout is not None
    content = stdout.strip()
    output = [
        list(map(maybe_parse, line.split("\t")))
        for line in content.split("\n")
    ]
    return output
