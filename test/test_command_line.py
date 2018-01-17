#!/usr/bin/env python
# encoding: utf-8
# vim: set ff=unix fenc=utf-8 et ts=4 sts=4 sta sw=4:
#
# test_spiral_matrix.py

import unittest
import argparse
from spiral_matrix.spiral_matrix import SpiralMatrix
from spiral_matrix.command_line import CommandLineInterface

################################################################################
class CommandLineArgumentsTestCase(unittest.TestCase):

    def setUp(self):
        self.cli = CommandLineInterface(caller=SpiralMatrix)

    def test_arg_is_int(self):

        pass_configs = [-1, 1.0, 90, 1.2e6, '3']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertEqual(self.cli.arg_is_int(config), int(config))

        fail_configs = [-0.01, 5.1, 1.2121e2, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(argparse.ArgumentError):
                    self.cli.arg_is_int(config)

    def test_arg_is_gt0(self):

        pass_configs = [2, 7.4, 17, 1.2121e2, '3']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertIs(self.cli.arg_is_gt0(config), config)

        fail_configs = [-20, -0.0001, 0, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(argparse.ArgumentError):
                    self.cli.arg_is_gt0(config)

    def test_arg_is_not0(self):

        pass_configs = [-2, 0.901, 1.2121e2, 17, '3']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertIs(self.cli.arg_is_not0(config), config)

        fail_configs = [0, 0.0, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(argparse.ArgumentError):
                    self.cli.arg_is_not0(config)

    def test_arg_is_odd_int(self):

        pass_configs = [-1, 1, 1.21e2, '3']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertIs(self.cli.arg_is_odd_int(config), int(config))

        fail_configs = [-20, 0, 2.999, 1.2121e2, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(argparse.ArgumentError):
                    self.cli.arg_is_odd_int(config)

    def test_arg_is_not0_int(self):

        pass_configs = [-1, 4.0, 50]
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertIs(self.cli.arg_is_not0_int(config), int(config))

        fail_configs = [-0, 0, 0.9, 1.2121e2, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(argparse.ArgumentError):
                    self.cli.arg_is_not0_int(config)

    def test_arg_is_gt0_odd_int(self):

        pass_configs = [1, 3.0, 55, '3']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertIs(self.cli.arg_is_gt0_odd_int(config), int(config))

        fail_configs = [-2, 0, 6, 9.01, 1.2121e2, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(argparse.ArgumentError):
                    self.cli.arg_is_gt0_odd_int(config)

    def test_arg_is_bearing(self):

        pass_configs = ['e'] #, 'S', 'WEST']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertEqual(self.cli.arg_is_bearing(config), config.upper())

        fail_configs = ['foo'] #, 'F', 12, '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(argparse.ArgumentError):
                    self.cli.arg_is_bearing(config)

################################################################################
if __name__ == '__main__':
    unittest.main(verbosity=2)
