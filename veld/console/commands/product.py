# -*- coding: utf-8 -*-

from veld.console.commands._reducable import ReducableCommand
from veld.core.operators.product import ProductOperator


class ProductCommand(ReducableCommand):
    def __init__(self):
        super().__init__(
            operator=ProductOperator,
            name="product",
            title="Compute the product of values in the data stream",
        )
