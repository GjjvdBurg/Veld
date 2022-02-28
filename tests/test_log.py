# -*- coding: utf-8 -*-

"""Unit tests for log command

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import math
import os
import random
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
        with open(os.path.join(path), "w") as fp:
            fp.write("1\n")
            fp.write("2\n")
            fp.write("3\n")

        exp = "\n".join(["0.0", "0.6931471805599453", "1.0986122886681098"])

        app = build_application()
        tester = Tester(app)
        tester.test_command("log", [path])

        try:
            out = tester.get_stdout().strip()
            self.assertEqual(out, exp)
        finally:
            os.unlink(path)

    def test_log_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(os.path.join(path), "w") as fp:
            fp.write("21\n")
            fp.write("22\n")
            fp.write("23\n")

        exp = "\n".join(
            ["1.322219294733919", "1.3424226808222062", "1.3617278360175928"]
        )

        app = build_application()
        tester = Tester(app)
        tester.test_command("log", ['-b', '10', path])

        try:
            out = tester.get_stdout().strip()
            self.assertEqual(out, exp)
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()