#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for the max command

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


class MaxCommandTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_max_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    def test_max_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\n")
            fp.write("5\n")
            fp.write("6\n")

        exp = "6"

        app = build_application()
        tester = Tester(app)
        tester.test_command("max", [path])

        out = tester.get_stdout().strip()
        self.assertEqual(out, exp)

    def test_max_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("-1\t8\n")
            fp.write("5\t2\n")
            fp.write("6\t-10\n")
            fp.write("8\t11\n")

        exp = "8\t11"

        app = build_application()
        tester = Tester(app)
        tester.test_command("max", [path])

        out = tester.get_stdout().strip()
        self.assertEqual(out, exp)

    def test_max_3(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1 8\n")
            fp.write("5 2\n")
            fp.write("6 -10\n")
            fp.write("8 11\n")

        exp = "11"

        app = build_application()
        tester = Tester(app)
        tester.test_command("max", [path, "--flatten", "-s", " "])

        out = tester.get_stdout().strip()
        self.assertEqual(out, exp)


if __name__ == "__main__":
    unittest.main()
