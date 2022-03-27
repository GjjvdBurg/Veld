# -*- coding: utf-8 -*-

"""Unit tests for stream processor


"""

import math
import os
import shutil
import tempfile
import unittest

from veld.exceptions import StreamProcessingError
from veld.stream_processor import StreamProcessor

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

        sp = StreamProcessor(path)
        self.assertEqual(list(sp), [[1, 2], [3, 4]])

    def test_process_stream_sep_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(os.path.join(path), "w") as fp:
            fp.write("1,2\n")
            fp.write("3,4\n")

        sp = StreamProcessor(path, sep=",")
        self.assertEqual(list(sp), [[1, 2], [3, 4]])

    def test_process_stream_sep_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(os.path.join(path), "w") as fp:
            fp.write("1, 2\n")
            fp.write("3, 4\n")

        sp = StreamProcessor(path, sep=",")
        self.assertEqual(list(sp), [[1, 2], [3, 4]])

    def test_process_stream_invalid_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(os.path.join(path), "w") as fp:
            fp.write("1\t2\n")
            fp.write("3\ta\n")

        sp = StreamProcessor(path, ignore_invalid=False)
        with self.assertRaises(StreamProcessingError) as err:
            list(sp)
        self.assertEqual(err.exception._value, "a")

    def test_process_stream_invalid_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(os.path.join(path), "w") as fp:
            fp.write("1\t2\n")
            fp.write("3\ta\n")

        sp = StreamProcessor(path, ignore_invalid=True)
        parsed = list(sp)
        self.assertEqual(parsed[0], [1, 2])
        self.assertEqual(parsed[1][0], 3)
        self.assertTrue(math.isnan(parsed[1][1]))

    def test_process_stream_flatten_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(os.path.join(path), "w") as fp:
            fp.write("1\t2\n")
            fp.write("3\t4\n")

        sp = StreamProcessor(path, flatten=True, ignore_invalid=True)
        parsed = list(sp)
        self.assertEqual(parsed, [[1], [2], [3], [4]])

    def test_parse_numeric_1(self):
        sp = StreamProcessor()
        self.assertEqual(int(1), sp.parse_numeric("1"))
        self.assertEqual(float(5.5), sp.parse_numeric("5.5"))

    def test_parse_numeric_2(self):
        sp = StreamProcessor(ignore_invalid=False)
        with self.assertRaises(StreamProcessingError) as err:
            sp.parse_numeric("a")
        self.assertEqual(err.exception._value, "a")

        sp = StreamProcessor(ignore_invalid=True)
        self.assertTrue(math.isnan(sp.parse_numeric("a")))


if __name__ == "__main__":
    unittest.main()
