#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for the stdev command

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


class StandardDeviationCommandTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_var_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    def test_stdev_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            for i in range(30):
                fp.write(f"{i}\n")

        exp = "8.803408430829505"

        app = build_application()
        tester = Tester(app)
        tester.test_command("stdev", [path])

        try:
            out = tester.get_stdout().strip()
            self.assertEqual(out, exp)
        finally:
            os.unlink(path)

    def test_stdev_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            for i in range(50):
                fp.write(f"{i}\n")

        exp = "14.430869689661812"

        app = build_application()
        tester = Tester(app)
        tester.test_command("stdev", [path, "--population"])

        try:
            out = tester.get_stdout().strip()
            self.assertEqual(out, exp)
        finally:
            os.unlink(path)

    def test_stdev_3(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            for i in range(10):
                fp.write(f"{i} {i*2} {i*3}\n")

        exp = "3.0276503540974917 6.0553007081949835 9.082951062292475"

        app = build_application()
        tester = Tester(app)
        tester.test_command("stdev", [path, "-s", " "])

        try:
            out = tester.get_stdout().strip()
            self.assertEqual(out, exp)
        finally:
            os.unlink(path)

    def test_stdev_4(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            for i in range(10):
                fp.write(f"{i} {i*2} {i*3}\n")

        exp = "7.334378190976783"

        app = build_application()
        tester = Tester(app)
        tester.test_command("stdev", [path, "-s", " ", "--flatten"])

        try:
            out = tester.get_stdout().strip()
            self.assertEqual(out, exp)
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
