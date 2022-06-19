#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for log command

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


class LogCommandTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_log_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    def test_log_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\n")
            fp.write("2\n")
            fp.write("3\n")

        exp = "\n".join(["0.0", "0.6931471805599453", "1.0986122886681098"])

        app = build_application()
        tester = Tester(app)
        tester.test_command("log", [path])

        out = tester.get_stdout().strip()
        self.assertEqual(out, exp)

    def test_log_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("21\n")
            fp.write("22\n")
            fp.write("23\n")

        exp = "\n".join(
            ["1.322219294733919", "1.3424226808222062", "1.3617278360175928"]
        )

        app = build_application()
        tester = Tester(app)
        tester.test_command("log", ["-b", "10", path])

        out = tester.get_stdout().strip()
        self.assertEqual(out, exp)

    def test_log_3(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("2\t1\n")
            fp.write("4\t2\n")
            fp.write("8\t3\n")

        exp = "\n".join(
            [
                "\t".join(["1.0", "0.0"]),
                "\t".join(["2.0", "1.0"]),
                "\t".join(["3.0", "1.5849625007211563"]),
            ]
        )

        app = build_application()
        tester = Tester(app)
        tester.test_command("log", ["-b", "2", path])

        out = tester.get_stdout().strip()
        self.assertEqual(out, exp)


if __name__ == "__main__":
    unittest.main()
