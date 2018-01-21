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
class CommandLineInterfaceTestCase(unittest.TestCase):

    def setUp(self):

        self.cli = CommandLineInterface(caller=SpiralMatrix)

    def test_01_instantiation(self):

        self.assertIsInstance(self.cli, CommandLineInterface)
        self.assertEqual(self.cli.caller, SpiralMatrix)

    def test_02_configure_parser(self):

        self.assertIsInstance(
                self.cli.configure_parser(), argparse.ArgumentParser)

    def test_03_arg_is_odd_int(self):

        pass_configs = [-1, 1.0, 91, 1.2121e4, '33']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertEqual(self.cli.arg_is_odd_int(config), config)

        fail_configs = [-0.51, 0, 7.7, 1.2121e2, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(argparse.ArgumentTypeError):
                    self.cli.arg_is_odd_int(config)

    def test_04_arg_is_not0_int(self):

        pass_configs = [-1, 4.0, 50]
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertIs(self.cli.arg_is_not0_int(config), config)

        fail_configs = [-0, 0, 0.9, 1.2121e2, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(argparse.ArgumentTypeError):
                    self.cli.arg_is_not0_int(config)

    def test_05_arg_is_gt0_odd_int(self):

        pass_configs = [1, 3.0, 55, '3']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertIs(self.cli.arg_is_gt0_odd_int(config), config)

        fail_configs = [-2, 0, 6, 9.01, 1.2121e2, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(argparse.ArgumentTypeError):
                    self.cli.arg_is_gt0_odd_int(config)

    def test_06_arg_is_bearing(self):

        pass_configs = ['e', 'S', 'WEST']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertEqual(self.cli.arg_is_bearing(config), config)

        fail_configs = ['foo', 'F', 12, '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(argparse.ArgumentTypeError):
                    self.cli.arg_is_bearing(config)

    def test_07_arg_is_text_file(self):

        from os import path
        cwd = path.dirname(__file__)

        pass_configs = [
            f'{cwd}/test-input/3-letter-words.txt',
            f'{cwd}/test-input/5-letter-words.txt',
            f'{cwd}/test-input/lorem-ipsum.txt',
            f'{cwd}/test-input/empty.txt',
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertEqual(self.cli.arg_is_text_file(config), config)

        fail_configs = [
            f'{cwd}/test-input/binary.dat',
        ]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(argparse.ArgumentTypeError):
                    self.cli.arg_is_text_file(config)

################################################################################
if __name__ == '__main__':
    unittest.main(verbosity=2)
