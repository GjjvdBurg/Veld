#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for barcount command

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


class BarCountTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_barcount_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    @patch("veld.console.commands.barcount.BarCountCommand.plt")
    def test_barcount_1(self, mock_plt):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\n")
            fp.write("2\n")
            fp.write("2\n")
            fp.write("2\n")
            fp.write("1\n")
            fp.write("3\n")
            fp.write("4\n")
            fp.write("2\n")

        app = build_application()
        tester = Tester(app)
        tester.test_command("barcount", [path])

        self.assertEqual(
            mock_plt.mock_calls,
            [
                call.bar([0.0, 1.0, 2.0, 3.0], [2, 4, 1, 1], width=0.8),
                call.xticks([0, 1, 2, 3], [1, 2, 3, 4]),
                call.xlim(left=None, right=None),
                call.ylim(bottom=None, top=None),
                call.show(),
            ],
        )
        os.unlink(path)

    @patch("veld.console.commands.barcount.BarCountCommand.plt")
    def test_barcount_2(self, mock_plt):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1 3\n")
            fp.write("2 4\n")
            fp.write("2 5\n")
            fp.write("2 4\n")
            fp.write("1 3\n")
            fp.write("3 4\n")
            fp.write("4 1\n")
            fp.write("2 3\n")

        app = build_application()
        tester = Tester(app)
        tester.test_command(
            "barcount", [path, "--separator", " ", "--width", "0.5"]
        )

        self.assertEqual(
            mock_plt.mock_calls,
            [
                call.bar(
                    [-0.125, 0.875, 1.875, 2.875], [2, 4, 1, 1], width=0.25
                ),
                call.bar(
                    [0.125, 2.125, 3.125, 4.125], [1, 3, 3, 1], width=0.25
                ),
                call.xticks([0.0, 1.0, 2.0, 3.0, 4.0], [1, 2, 3, 4, 5]),
                call.xlim(left=None, right=None),
                call.ylim(bottom=None, top=None),
                call.show(),
            ],
        )
        os.unlink(path)

    @patch("veld.console.commands.barcount.BarCountCommand.plt")
    def test_barcount_3(self, mock_plt):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\n")
            fp.write("2\n")
            fp.write("2\n")
            fp.write("2\n")
            fp.write("1\n")
            fp.write("3\n")
            fp.write("4\n")
            fp.write("2\n")

        app = build_application()
        tester = Tester(app)
        tester.test_command("barcount", [path, "--relative", "--width", "0.5"])

        self.assertEqual(
            mock_plt.mock_calls,
            [
                call.bar(
                    [0.0, 1.0, 2.0, 3.0], [0.25, 0.5, 0.125, 0.125], width=0.5
                ),
                call.xticks([0, 1, 2, 3], [1, 2, 3, 4]),
                call.xlim(left=None, right=None),
                call.ylim(bottom=None, top=None),
                call.show(),
            ],
        )
        os.unlink(path)

    @patch("veld.console.commands.barcount.BarCountCommand.plt")
    def test_barcount_4(self, mock_plt):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("a c\n")
            fp.write("b d\n")
            fp.write("b e\n")
            fp.write("b d\n")
            fp.write("a c\n")
            fp.write("c d\n")
            fp.write("d a\n")
            fp.write("b c\n")

        app = build_application()
        tester = Tester(app)
        tester.test_command(
            "barcount", [path, "--separator", " ", "--width", "0.5"]
        )

        self.assertEqual(
            mock_plt.mock_calls,
            [
                call.bar(
                    [-0.125, 0.875, 1.875, 2.875], [2, 4, 1, 1], width=0.25
                ),
                call.bar(
                    [0.125, 2.125, 3.125, 4.125], [1, 3, 3, 1], width=0.25
                ),
                call.xticks([0, 1, 2, 3, 4], ["a", "b", "c", "d", "e"]),
                call.xlim(left=None, right=None),
                call.ylim(bottom=None, top=None),
                call.show(),
            ],
        )
        os.unlink(path)


if __name__ == "__main__":
    unittest.main()
