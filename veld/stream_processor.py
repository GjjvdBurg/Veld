# -*- coding: utf-8 -*-

"""Definitions for processing a data stream

This file is part of the Veld package.

Author: G.J.J. van den Burg
License: See the LICENSE file
Copyright: (c) 2022, G.J.J. van den Burg

"""

import abc
import sys

from typing import Generic
from typing import Iterator
from typing import List
from typing import Optional
from typing import TextIO
from typing import TypeVar
from typing import Union

from veld.exceptions import StreamProcessingError
from veld.utils import parse_numeric

T = TypeVar("T")


class BaseStreamProcessor(Generic[T]):
    def __init__(
        self,
        path: Optional[str] = None,
        sep: Optional[str] = None,
        encoding: str = "utf-8",
        flatten: bool = False,
        ignore_invalid: bool = False,
    ):
        self._path = path
        self._sep = sep
        self._ignore_invalid = ignore_invalid
        self._encoding = encoding
        self._flatten = flatten

        self._stream: Optional[TextIO] = None
        self._stream_iter: Optional[Iterator[List[T]]] = None
        self._last_line: Optional[str] = None

    @property
    def stream(self) -> TextIO:
        """Return the stream that we're reading from"""
        if self._stream is not None:
            return self._stream
        if self._path is None:
            self._stream = sys.stdin
        else:
            self._stream = open(self._path, "r", encoding=self._encoding)
        return self._stream

    @property
    def last_line(self) -> Optional[str]:
        """The most recently parsed line"""
        return self._last_line

    def close_stream(self):
        if self._stream is None:
            return
        if self._stream == sys.stdin:
            return
        self._stream.close()

    def __iter__(self) -> "BaseStreamProcessor":
        self._stream_iter = self.process_stream()
        return self

    def __next__(self) -> List[T]:
        assert self._stream_iter is not None
        return next(self._stream_iter)

    def process_stream(self) -> Iterator[List[T]]:
        """Process the input stream"""
        for line in self.stream:
            self._last_line = line

            # Skip empty lines
            if not line.strip():
                continue

            # Split the line in case of multidimensional data
            parts = line.split(sep=self._sep)

            # Parse numbers from text
            values = list(map(self._parse, parts))

            # Flatten the input array if desired
            if self._flatten:
                for value in values:
                    yield [value]
            else:
                yield values
        self.close_stream()

    @abc.abstractmethod
    def _parse(self, x: str) -> T:
        pass


class NumericStreamProcessor(BaseStreamProcessor[float]):
    def _parse(self, x: str) -> float:
        """Parse a string number, preserving type"""
        x = x.rstrip("\r\n")
        try:
            return parse_numeric(x)
        except ValueError:
            pass
        if self._ignore_invalid:
            return float("nan")
        self.close_stream()
        raise StreamProcessingError(x)


class ForgivingStreamProcessor(BaseStreamProcessor[Union[float, str]]):
    def _parse(self, x: str) -> Union[str, float]:
        """Parse a string number, preserving type"""
        x = x.rstrip("\r\n")
        try:
            return parse_numeric(x)
        except ValueError:
            pass
        return x
