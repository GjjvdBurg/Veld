#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit tests for stream processor

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import math
import os
import shutil
import tempfile
import unittest

from veld.exceptions import StreamProcessingError
from veld.stream_processor import ForgivingStreamProcessor
from veld.stream_processor import NumericStreamProcessor

# TODO:
# - encoding
# - test with mock stdin


class StreamProcessorTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_sp_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    def test_process_stream_base(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(os.path.join(path), "w") as fp:
            fp.write("1\t2\n")
            fp.write("3\t4\n")

        sp = NumericStreamProcessor(path)
        self.assertEqual(list(sp), [[1, 2], [3, 4]])

    def test_process_stream_sep_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(os.path.join(path), "w") as fp:
            fp.write("1,2\n")
            fp.write("3,4\n")

        sp = NumericStreamProcessor(path, sep=",")
        self.assertEqual(list(sp), [[1, 2], [3, 4]])

    def test_process_stream_sep_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(os.path.join(path), "w") as fp:
            fp.write("1, 2\n")
            fp.write("3, 4\n")

        sp = NumericStreamProcessor(path, sep=",")
        self.assertEqual(list(sp), [[1, 2], [3, 4]])

    def test_process_stream_invalid_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(os.path.join(path), "w") as fp:
            fp.write("1\t2\n")
            fp.write("3\ta\n")

        sp = NumericStreamProcessor(path, ignore_invalid=False)
        with self.assertRaises(StreamProcessingError) as err:
            list(sp)
        self.assertEqual(err.exception._value, "a")

    def test_process_stream_invalid_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(os.path.join(path), "w") as fp:
            fp.write("1\t2\n")
            fp.write("3\ta\n")

        sp = NumericStreamProcessor(path, ignore_invalid=True)
        parsed = list(sp)
        self.assertEqual(parsed[0], [1, 2])
        self.assertEqual(parsed[1][0], 3)
        self.assertTrue(math.isnan(parsed[1][1]))

    def test_process_stream_flatten_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(os.path.join(path), "w") as fp:
            fp.write("1\t2\n")
            fp.write("3\t4\n")

        sp = NumericStreamProcessor(path, flatten=True, ignore_invalid=True)
        parsed = list(sp)
        self.assertEqual(parsed, [[1], [2], [3], [4]])

    def test_parse_1(self):
        sp = NumericStreamProcessor()
        self.assertEqual(int(1), sp._parse("1"))
        self.assertEqual(float(5.5), sp._parse("5.5"))

    def test_parse_2(self):
        sp = NumericStreamProcessor(ignore_invalid=False)
        with self.assertRaises(StreamProcessingError) as err:
            sp._parse("a")
        self.assertEqual(err.exception._value, "a")

        sp = NumericStreamProcessor(ignore_invalid=True)
        self.assertTrue(math.isnan(sp._parse("a")))

    def test_parse_3(self):
        sp = ForgivingStreamProcessor()
        self.assertEqual(int(1), sp._parse("1"))
        self.assertEqual(float(5.5), sp._parse("5.5"))
        self.assertEqual("abc", sp._parse("abc"))

    @unittest.skip("not implemented yet")
    def test_encoding(self):
        pass

    @unittest.skip("not implemented yet")
    def test_parse_stdin(self):
        pass


if __name__ == "__main__":
    unittest.main()
