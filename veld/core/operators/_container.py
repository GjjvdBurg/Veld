# -*- coding: utf-8 -*-

"""Container for operator results"""


from dataclasses import dataclass

from typing import Optional
from typing import Union


@dataclass(frozen=True)
class BaseResultContainer:
    pass


@dataclass(frozen=True)
class SingleResultContainer(BaseResultContainer):
    value: Union[float, str]


@dataclass(frozen=True)
class SingleResultContainerNumeric(SingleResultContainer):
    value: float


@dataclass(frozen=True)
class SummaryResultContainer(BaseResultContainer):
    count: Union[float, str]
    maximum: Union[float, str]
    minimum: Union[float, str]
    mean: Optional[float]
    mode: Union[float, str]
    total: Optional[float]
