#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for round command

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


class RoundCommandTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_round_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    def test_round_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1.89255\n")
            fp.write("8.47887\n")
            fp.write("6.15849\n")

        exp = "\n".join(["2", "8", "6"])

        app = build_application()
        tester = Tester(app)
        tester.test_command("round", [path])

        out = tester.get_stdout().strip()
        self.assertEqual(out, exp)

    def test_round_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("1.89255\n")
            fp.write("8.47887\n")
            fp.write("6.15849\n")

        exp = "\n".join(["1.89", "8.48", "6.16"])

        app = build_application()
        tester = Tester(app)
        tester.test_command("round", [path, "-n", "2"])

        out = tester.get_stdout().strip()
        self.assertEqual(out, exp)

    def test_round_3(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("0.58835,0.6149\n")
            fp.write("0.86463,0.2592\n")
            fp.write("0.64814,0.16424\n")

        exp = "\n".join(["0.588,0.615", "0.865,0.259", "0.648,0.164"])

        app = build_application()
        tester = Tester(app)
        tester.test_command("round", ["-s", ",", "-n", "3", path])

        out = tester.get_stdout().strip()
        self.assertEqual(out, exp)


if __name__ == "__main__":
    unittest.main()
