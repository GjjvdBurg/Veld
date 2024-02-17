# -*- coding: utf-8 -*-

"""Container for operator results"""


from dataclasses import dataclass


@dataclass(frozen=True)
class BaseResultContainer:
    pass


@dataclass(frozen=True)
class SingleResultContainer(BaseResultContainer):
    value: float


@dataclass(frozen=True)
class SummaryResultContainer(BaseResultContainer):
    count: float
    maximum: float
    minimum: float
    mean: float
    mode: float
    total: float
