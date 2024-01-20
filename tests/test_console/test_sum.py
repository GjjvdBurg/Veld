#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for the sum command

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
from veld.exceptions import StreamProcessingError


class SumCommandTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_sum_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    def test_sum_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\n")
            fp.write("5\n")
            fp.write("6\n")

        exp = "12"

        app = build_application()
        tester = Tester(app)
        tester.test_command("sum", [path])

        stdout = tester.get_stdout()
        assert stdout is not None
        out = stdout.strip()
        self.assertEqual(out, exp)

    def test_sum_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("-1\t8\n")
            fp.write("5\t2\n")
            fp.write("6\t-10\n")
            fp.write("8\t1\n")

        exp = "18\t1"

        app = build_application()
        tester = Tester(app)
        tester.test_command("sum", [path])

        stdout = tester.get_stdout()
        assert stdout is not None
        out = stdout.strip()
        self.assertEqual(out, exp)

    def test_sum_3(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\t8\n")
            fp.write("5\t2\n")
            fp.write("6\t-10\n")
            fp.write("8\t1\n")

        exp = "21"

        app = build_application()
        tester = Tester(app)
        tester.test_command("sum", [path, "--flatten"])

        stdout = tester.get_stdout()
        assert stdout is not None
        out = stdout.strip()
        self.assertEqual(out, exp)

    def test_sum_4a(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("5\n")
            fp.write("1\n")
            fp.write("null\n")
            fp.write("6\n")
            fp.write("8\n")

        app = build_application()
        tester = Tester(app)
        with self.assertRaises(StreamProcessingError) as cm:
            tester.test_command("sum", [path])

        exception = cm.exception
        self.assertEqual(exception._value, "null")

    def test_sum_4b(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("5\n")
            fp.write("1\n")
            fp.write("null\n")
            fp.write("6\n")
            fp.write("8\n")

        exp = "20"

        app = build_application()
        tester = Tester(app)
        tester.test_command("sum", [path, "--ignore"])

        stdout = tester.get_stdout()
        assert stdout is not None
        out = stdout.strip()
        self.assertEqual(out, exp)

    def test_sum_5(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\t8\n")
            fp.write("5\t2\n")
            fp.write("6\t-10\n")
            fp.write("8\t1\n")

        exp = "\n".join(["9", "7", "-4", "9"])

        app = build_application()
        tester = Tester(app)
        tester.test_command("sum", [path, "--reduce"])

        stdout = tester.get_stdout()
        assert stdout is not None
        out = stdout.strip()
        self.assertEqual(out, exp)


if __name__ == "__main__":
    unittest.main()
