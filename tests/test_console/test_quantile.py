#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for the quantile command

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


class QuantileCommandTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_quantile_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    def test_quantile_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\n")
            fp.write("5\n")
            fp.write("6\n")
            fp.write("7\n")
            fp.write("2\n")
            fp.write("0\n")

        exp = "5.9"

        app = build_application()
        tester = Tester(app)
        tester.test_command("quantile", ["-q", "0.78", path])

        stdout = tester.get_stdout()
        assert stdout is not None
        out = stdout.strip()
        self.assertEqual(out, exp)

    def test_quantile_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\t8\n")
            fp.write("5\t2\n")
            fp.write("6\t1\n")
            fp.write("8\t1\n")

        exp = "6.5\t3.5"

        app = build_application()
        tester = Tester(app)
        tester.test_command("quantile", ["-q", "0.75", path])

        stdout = tester.get_stdout()
        assert stdout is not None
        out = stdout.strip()
        self.assertEqual(out, exp)

    def test_quantile_3(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\t8\n")
            fp.write("5\t2\n")
            fp.write("6\t1\n")
            fp.write("8\t1\n")

        exp = "1.1"

        app = build_application()
        tester = Tester(app)
        tester.test_command(
            "quantile", [path, "--flatten", "--quantile", "0.3"]
        )

        stdout = tester.get_stdout()
        assert stdout is not None
        out = stdout.strip()
        self.assertEqual(out, exp)


if __name__ == "__main__":
    unittest.main()
