# -*- coding: utf-8 -*-

"""Unit tests for the variance command

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


class VarianceCommandTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_var_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    def test_variance_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            for i in range(20):
                fp.write(f"{i}\n")

        exp = "35.0"

        app = build_application()
        tester = Tester(app)
        tester.test_command("variance", [path])

        try:
            out = tester.get_stdout().strip()
            self.assertEqual(out, exp)
        finally:
            os.unlink(path)

    def test_variance_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            for i in range(20):
                fp.write(f"{i}\n")

        exp = "33.25"

        app = build_application()
        tester = Tester(app)
        tester.test_command("variance", [path, "--population"])

        try:
            out = tester.get_stdout().strip()
            self.assertEqual(out, exp)
        finally:
            os.unlink(path)

    def test_variance_3(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            for i in range(10):
                fp.write(f"{i} {i*2} {i*3}\n")

        exp = "9.166666666666666 36.666666666666664 82.5"

        app = build_application()
        tester = Tester(app)
        tester.test_command("variance", [path, "-s", " "])

        try:
            out = tester.get_stdout().strip()
            self.assertEqual(out, exp)
        finally:
            os.unlink(path)

    def test_variance_4(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            for i in range(10):
                fp.write(f"{i} {i*2} {i*3}\n")

        exp = "53.793103448275865"

        app = build_application()
        tester = Tester(app)
        tester.test_command("variance", [path, "-s", " ", "--flatten"])

        try:
            out = tester.get_stdout().strip()
            self.assertEqual(out, exp)
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
