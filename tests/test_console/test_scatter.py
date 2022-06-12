#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for the scatter command

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import os
import shutil
import tempfile
import unittest

from unittest.mock import call
from unittest.mock import patch

from wilderness import Tester

from veld.console import build_application


class ScatterTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_scatter_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    @patch("veld.console.commands.scatter.ScatterPlotCommand.plt")
    def test_scatter_1(self, mock_plt):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            for i in range(10):
                fp.write(f"{i} {i*i}\n")

        app = build_application()
        tester = Tester(app)
        tester.test_command("scatter", [path, "--separator", " "])

        self.assertEqual(
            mock_plt.mock_calls,
            [
                call.scatter(list(range(10)), [i * i for i in range(10)]),
                call.xlim(left=None, right=None),
                call.ylim(bottom=None, top=None),
                call.show(),
            ],
        )
        os.unlink(path)

    @patch("veld.console.commands.scatter.ScatterPlotCommand.plt")
    def test_scatter_2(self, mock_plt):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            for i in range(10):
                fp.write(f"{i} {i*i}\n")

        app = build_application()
        tester = Tester(app)
        tester.test_command(
            "scatter",
            [
                path,
                "--separator",
                " ",
                "--ymin",
                "-1",
                "--xlabel",
                "x",
                "--ylabel",
                "y",
                "--title",
                "title",
            ],
        )

        self.assertEqual(
            mock_plt.mock_calls,
            [
                call.scatter(list(range(10)), [i * i for i in range(10)]),
                call.xlim(left=None, right=None),
                call.ylim(bottom=-1, top=None),
                call.xlabel("x"),
                call.ylabel("y"),
                call.title("title"),
                call.show(),
            ],
        )
        os.unlink(path)

    @patch("veld.console.commands.scatter.ScatterPlotCommand.plt")
    def test_scatter_3(self, mock_plt):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("\t".join([f"{i}" for i in range(10)]) + "\n")
            fp.write("\t".join([f"{i*i}" for i in range(10)]) + "\n")

        app = build_application()
        tester = Tester(app)
        tester.test_command("scatter", [path, "--transpose"])

        self.assertEqual(
            mock_plt.mock_calls,
            [
                call.scatter(list(range(10)), [i * i for i in range(10)]),
                call.xlim(left=None, right=None),
                call.ylim(bottom=None, top=None),
                call.show(),
            ],
        )
        os.unlink(path)


if __name__ == "__main__":
    unittest.main()
