from typing import Union


def parse_numeric(text: str) -> Union[float, int]:
    """Parse a number, maintaining the int/float type

    Raises ValueError if parsing fails.

    """
    if "." in text or "e" in text:
        return float(text)
    return int(text)
