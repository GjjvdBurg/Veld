# -*- coding: utf-8 -*-

"""Unit tests for the min command

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


class MinCommandTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_min_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    def test_min_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\n")
            fp.write("5\n")
            fp.write("6\n")

        exp = "1"

        app = build_application()
        tester = Tester(app)
        tester.test_command("min", [path])

        try:
            out = tester.get_stdout().strip()
            self.assertEqual(out, exp)
        finally:
            os.unlink(path)

    def test_min_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("-1\t8\n")
            fp.write("5\t2\n")
            fp.write("6\t-10\n")
            fp.write("8\t1\n")

        exp = "-1\t-10"

        app = build_application()
        tester = Tester(app)
        tester.test_command("min", [path])

        try:
            out = tester.get_stdout().strip()
            self.assertEqual(out, exp)
        finally:
            os.unlink(path)

    def test_min_3(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\t8\n")
            fp.write("5\t2\n")
            fp.write("6\t-10\n")
            fp.write("8\t1\n")

        exp = "-10"

        app = build_application()
        tester = Tester(app)
        tester.test_command("min", [path, "--flatten"])

        try:
            out = tester.get_stdout().strip()
            self.assertEqual(out, exp)
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
