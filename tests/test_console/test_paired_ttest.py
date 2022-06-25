#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for paired t-test command

Author: G.J.J. van den Burg
Copyright: (c) 2022, G.J.J. van den Burg
License: See LICENSE file.

"""

import json
import os
import shutil
import tempfile
import unittest

from wilderness import Tester

from veld.console import build_application


class PairedTTestCommandTestCase(unittest.TestCase):
    def setUp(self):
        self._working_dir = tempfile.mkdtemp(prefix="veld_test_paired_ttest_")

    def tearDown(self):
        shutil.rmtree(self._working_dir)

    def test_paired_ttest_1(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("-0.5806804308560377\t0.6265129697573907\n")
            fp.write("0.85959847518418140\t1.5053476466075848\n")
            fp.write("1.30726452291435450\t2.3150974331355956\n")
            fp.write("2.47681609282295300\t3.9534878734426620\n")
            fp.write("3.74548545477386650\t4.7670543311902100\n")
            fp.write("4.97740342757478600\t5.8702515005003450\n")
            fp.write("5.32958684584713400\t6.3295895050860950\n")
            fp.write("6.63436663007075300\t7.4541652826874850\n")
            fp.write("7.14404502760195400\t8.8034745945957180\n")
            fp.write("8.43620886695391000\t9.3329243799127980\n")

        exp = "Test statistic = -10.960326\npvalue = 1.65973e-06"

        app = build_application()
        tester = Tester(app)
        tester.test_command("paired-ttest", [path])

        out = tester.get_stdout().strip()
        self.assertEqual(out, exp)

    def test_paired_ttest_2(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("0.79681407295615030\t+1.59415700808159260\n")
            fp.write("0.35755522950674856\t+1.68718658266329550\n")
            fp.write("0.12662349004303430\t+0.46130482124207567\n")
            fp.write("0.38251576944664156\t+2.04091227756236300\n")
            fp.write("0.33686244271671150\t-0.65065173849964110\n")
            fp.write("0.81594408993556200\t-0.51677844203518340\n")
            fp.write("0.12620914324684718\t+0.30464970409307895\n")
            fp.write("0.93886879841359470\t+1.86095839658110760\n")
            fp.write("0.34151387120157695\t-1.74426251866327390\n")
            fp.write("0.74631833353583620\t-0.07064276845905516\n")

        exp = "Test statistic = 0.000608\npvalue = 0.999528"

        app = build_application()
        tester = Tester(app)
        tester.test_command("paired-ttest", [path])

        out = tester.get_stdout().strip()
        self.assertEqual(out, exp)

    def test_paired_ttest_3(self):
        path = os.path.join(self._working_dir, "stream.txt")
        with open(path, "w") as fp:
            fp.write("-0.92233525314803990\t-1.428129933596292000\n")
            fp.write("+0.04436014759148722\t+0.010011560726471148\n")
            fp.write("+0.74580878863057310\t-0.103621091410129600\n")
            fp.write("+1.11757960971542470\t+0.305503019640337200\n")
            fp.write("-0.32543714098325216\t-0.694482872800190000\n")
            fp.write("+0.61577174490612290\t+0.197385670486872220\n")
            fp.write("+1.52886139957528330\t+0.954379068639977000\n")
            fp.write("+1.55341904398311770\t+1.051079076337888800\n")
            fp.write("+1.75370599687042720\t+1.192955214843334000\n")
            fp.write("+1.14131380499853790\t+0.342914318906971600\n")

        exp_obj = {
            "statistic": 7.001208928439045,
            "dof": 9,
            "pvalue": 6.316304505558856e-05,
            "reject_H0_at_0.05": True,
            "mean_difference": 0.5425054110364441,
            "std_difference": 0.2450366442961591,
            "count": 10,
        }

        app = build_application()
        tester = Tester(app)
        tester.test_command("paired-ttest", [path, "--json"])

        out = tester.get_stdout().strip()
        out_lines = out.split("\n")
        self.assertTrue(
            all(map(lambda x: x.startswith("\t"), out_lines[1:-1]))
        )
        self.assertEqual(out_lines[0], "{")
        self.assertEqual(out_lines[-1], "}")

        out_obj = json.loads(out)
        self.assertEqual(out_obj["dof"], exp_obj["dof"])
        self.assertEqual(out_obj["count"], exp_obj["count"])
        self.assertEqual(
            out_obj["reject_H0_at_0.05"], exp_obj["reject_H0_at_0.05"]
        )
        self.assertAlmostEqual(
            out_obj["statistic"], exp_obj["statistic"], places=12
        )
        self.assertAlmostEqual(out_obj["pvalue"], exp_obj["pvalue"], places=12)
        self.assertAlmostEqual(
            out_obj["mean_difference"], exp_obj["mean_difference"], places=12
        )
        self.assertAlmostEqual(
            out_obj["std_difference"], exp_obj["std_difference"], places=12
        )


if __name__ == "__main__":
    unittest.main()
