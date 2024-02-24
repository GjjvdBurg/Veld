# -*- coding: utf-8 -*-

import abc

from typing import Optional

from veld.core.operators._container import BaseResultContainer


class BaseOperator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        """Initialize the operator"""

    @abc.abstractproperty
    def result(self) -> Optional[BaseResultContainer]:
        """Return the collected result of this operator"""

    @abc.abstractmethod
    def update(self, value: float) -> None:
        """Update this operator with a given value"""
