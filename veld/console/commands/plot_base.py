# -*- coding: utf-8 -*-

import importlib

from types import ModuleType

from .base import BaseCommand


class BasePlotCommand(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._plt = None

    @property
    def plt(self) -> ModuleType:
        # This is here for lazy evaluation, as it is only needed for the
        # plotting commands and otherwise slows down all veld commands.
        if self._plt is None:
            self._plt = importlib.import_module("matplotlib.pyplot")
        return self._plt

    def register(self) -> None:
        super().register()
        self.add_argument(
            "--xmin", help="Lower limit of the horizontal axis", type=float
        )
        self.add_argument(
            "--xmax", help="Upper limit of the horizontal axis", type=float
        )
        self.add_argument(
            "--ymin", help="Lower limit of the vertical axis", type=float
        )
        self.add_argument(
            "--ymax", help="Upper limit of the vertical axis", type=float
        )
        self.add_argument(
            "--xlabel", help="Axis label for the horizontal axis"
        )
        self.add_argument(
            "--ylabel",
            help="Axis label for the vertical axis",
        )
        self.add_argument("--title", help="Title for the plot")

    def set_plot_attributes(self) -> None:
        # Set common plot options
        self.plt.xlim(left=self.args.xmin, right=self.args.xmax)
        self.plt.ylim(bottom=self.args.ymin, top=self.args.ymax)
        if self.args.xlabel is not None:
            self.plt.xlabel(self.args.xlabel)
        if self.args.ylabel is not None:
            self.plt.ylabel(self.args.ylabel)
        if self.args.title:
            self.plt.title(self.args.title)
