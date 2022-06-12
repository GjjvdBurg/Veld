#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import tempfile
import unittest

from unittest.mock import call
from unittest.mock import patch

from wilderness import Tester

from veld.console import build_application


class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_lineplot_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    @patch("veld.console.commands.lineplot.LinePlotCommand.plt")
    def test_lineplot_1(self, mock_plt):
        path = os.path.join(self._working_dir, "stream.txt")
        x = list(range(10))
        y = [i * i for i in x]
        with open(path, "w") as fp:
            for xx, yy in zip(x, y):
                fp.write(f"{xx}\t{yy}\n")

        app = build_application()
        tester = Tester(app)
        tester.test_command("lineplot", [path, "--consolidate", "--have-x"])

        self.assertEqual(
            mock_plt.mock_calls,
            [
                call.scatter(x, y),
                call.plot(x, y),
                call.xlim(left=None, right=None),
                call.ylim(bottom=None, top=None),
                call.show(),
            ],
        )
