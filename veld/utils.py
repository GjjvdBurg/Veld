from typing import Union


def parse_numeric(text: str) -> Union[float, int]:
    """Parse a number, maintaining the int/float type

    Raises ValueError if parsing fails.

    """
    func = float if "." in text else int
    return func(text)
