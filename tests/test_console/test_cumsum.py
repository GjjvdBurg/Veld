#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for cumsum command

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import os
import shutil
import tempfile
import unittest

from wilderness import Tester

from veld.console import build_application


class CumSumCommandTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_cumsum_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    def test_cumsum_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\n")
            fp.write("3\n")
            fp.write("5\n")

        exp = "\n".join(["1", "4", "9"])

        app = build_application()
        tester = Tester(app)
        tester.test_command("cumsum", [path])

        out = tester.get_stdout().strip()
        self.assertEqual(out, exp)

    def test_cumsum_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1 2\n")
            fp.write("3 4\n")
            fp.write("5 6\n")

        exp = "\n".join(["1 2", "4 6", "9 12"])

        app = build_application()
        tester = Tester(app)
        tester.test_command("cumsum", [path, "--separator", " "])

        out = tester.get_stdout().strip()
        self.assertEqual(out, exp)

    def test_cumsum_3(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1 2\n")
            fp.write("3 4\n")
            fp.write("5 6\n")

        exp = "\n".join(["1", "3", "6", "10", "15", "21"])

        app = build_application()
        tester = Tester(app)
        tester.test_command("cumsum", [path, "--separator", " ", "--flatten"])

        out = tester.get_stdout().strip()
        self.assertEqual(out, exp)


if __name__ == "__main__":
    unittest.main()
