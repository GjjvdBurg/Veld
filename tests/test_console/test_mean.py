#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for the mean command

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


class MeanCommandTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_mean_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    def test_mean_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\n")
            fp.write("5\n")
            fp.write("6\n")

        exp = "4.0"

        app = build_application()
        tester = Tester(app)
        tester.test_command("mean", [path])

        stdout = tester.get_stdout()
        assert stdout is not None
        out = stdout.strip()
        self.assertEqual(out, exp)

    def test_mean_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\t8\n")
            fp.write("5\t2\n")
            fp.write("6\t1\n")
            fp.write("8\t1\n")

        exp = "5.0\t3.0"

        app = build_application()
        tester = Tester(app)
        tester.test_command("mean", [path])

        stdout = tester.get_stdout()
        assert stdout is not None
        out = stdout.strip()
        self.assertEqual(out, exp)

    def test_mean_3(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\t8\n")
            fp.write("5\t2\n")
            fp.write("6\t1\n")
            fp.write("8\t1\n")

        exp = "4.0"

        app = build_application()
        tester = Tester(app)
        tester.test_command("mean", [path, "--flatten"])

        stdout = tester.get_stdout()
        assert stdout is not None
        out = stdout.strip()
        self.assertEqual(out, exp)

    def test_mean_4(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1\t8\n")
            fp.write("5\t2\n")
            fp.write("6\t1\n")
            fp.write("8\t1\n")

        exp = "\n".join(["4.5", "3.5", "3.5", "4.5"])

        app = build_application()
        tester = Tester(app)
        tester.test_command("mean", [path, "--reduce"])

        stdout = tester.get_stdout()
        assert stdout is not None
        out = stdout.strip()
        self.assertEqual(out, exp)


if __name__ == "__main__":
    unittest.main()
