#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# test_spiral_matrix.py

import unittest
from spiral_matrix.spiral_matrix import SpiralMatrix, ArgumentError
from spiral_matrix.spiral_matrix import _is_int, _is_gt0, _is_not0
from spiral_matrix.spiral_matrix import _is_odd_int, _is_not0_int
from spiral_matrix.spiral_matrix import _is_gt0_odd_int, _is_bearing

class SpiralMatrixInstantiationTestCase(unittest.TestCase):

    def test_simple_instantiation(self):

        pass_configs = [3, 5, 23, 1.21e2, '3']
        for config in pass_configs:
            with self.subTest(config=config):
                m = SpiralMatrix(config)
                self.assertIsInstance(m, SpiralMatrix)

        fail_configs = [-3, 0, 2.3, 1.21e-1, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(AttributeError):
                    m = SpiralMatrix(config)

    def test_build(self):

        pass_configs = [
            { 'dimension': 5, 'axes': False, 'right': False, 'bearing': 'E',
              'start': 1, 'step': 1, 'file': None, 'words': None,
              'want_matrix': [[17, 16, 15, 14, 13],
                              [18,  5,  4,  3, 12],
                              [19,  6,  1,  2, 11],
                              [20,  7,  8,  9, 10],
                              [21, 22, 23, 24, 25]] },
            { 'dimension': 3, 'axes': True, 'right': True, 'bearing': 'N',
              'start': 1, 'step': 1, 'file': None,
              'words': 'eenie meenie minie moe',
              'want_matrix': [['eenie', 'meenie', 'minie'],
                              [  'moe',  'eenie',   'moe'],
                              ['minie', 'meenie', 'eenie']] },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                dimension, axes, right, bearing, start, step, file, words, \
                        want_matrix = config.values()
                m = SpiralMatrix(dimension, axes, right, bearing, start, step,
                        file, words)
                self.assertEqual(m.matrix, want_matrix)

class SpiralMatrixMethodsTestCase(unittest.TestCase):

    def setUp(self):

        self.matrix_dimension = 5

    def test_series(self):

        m = SpiralMatrix(self.matrix_dimension)

        pass_configs = [
            { 'start': 1, 'step': 1,
              'want_0_0_value': 17 },
            { 'start': 1000, 'step': 2,
              'want_0_0_value': 1032 },
            { 'start': -100, 'step': 3,
              'want_0_0_value': -52 },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                m.start, m.step, want_value = config.values()
                m.series = m._series()
                self.assertIsInstance(m.series, range)
                self.assertEqual(len(m.series), m.max)
                m._build()
                self.assertEqual(m.matrix[0][0], want_0_0_value)

    def test_series_from_string(self):

        m = SpiralMatrix(self.matrix_dimension)

        pass_configs = [
            { 'words': 'vulture duck crocodile elephant tiger',
              'want_0_0_value': 'duck' },
            { 'words': '10 4 2 45 31 8.88 22 -7 0 94',
              'want_0_0_value': '22' },
            { 'words': '~ @#$ ) ( !*% +!',
              'want_0_0_value': '!*%' },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                m.words, want_value = config.values()
                m.series = m._series_from_string()
                self.assertIsInstance(m.series, list)
                self.assertEqual(len(m.series), m.max)
                m._build()
                self.assertEqual(m.matrix[0][0], want_0_0_value)

    def test_series_from_file(self):

        m = SpiralMatrix(self.matrix_dimension)

        # import os
        # file_path = '%s/input' % (os.path.dirname(os.path.abspath(__file__)))
        # pass_configs = ['tests/input/%s' % (f) for f in os.listdir(file_path)]

        pass_configs = [
            { 'filename': 'test/test-input/5-letter-words.txt',
              'want_0_0_value': 'alike' },
            { 'filename': 'test/test-input/3-letter-words.txt',
              'want_0_0_value': 'alt' },
            { 'filename': 'test/test-input/lorem-ipsum.txt',
              'want_0_0_value': 'at.' },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                filename, want_value = config.values()
                with open(filename) as file:
                    m.file = file
                    m.series = m._series_from_file()
                    self.assertIsInstance(m.series, list)
                    self.assertEqual(len(m.series), m.max)
                    m._build()
                    self.assertEqual(m.matrix[0][0], want_0_0_value)

        # fail_configs = [
        #     { 'filename': 'tests/input/binary.dat' },
        #     { 'filename': 'tests/input/empty.txt' },
        # ]
        # for config in fail_configs:
        #     with self.subTest(config=config):
        #         filename, = config.values()
        #         with open(filename) as file:
        #             m.file = file
        #             with self.assertRaises(ArgumentError):
        #                 m.series = m._series_from_file()

    def test_width(self):

        m = SpiralMatrix(self.matrix_dimension)

        pass_configs = [
            { 'series': ['vulture', 'duck', 'crocodile', 'elephant', 'tiger'],
              'want_width': 9 },
            { 'series': range(90, 110, 2),
              'want_width': 3 },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                m.series, want_width = config.values()
                m.width = m._width()
                self.assertIsInstance(m.width, int)
                self.assertEqual(m.width, want_width)

    def test_fill(self):

        m = SpiralMatrix(self.matrix_dimension)

        pass_configs = [
            { 'series': ['vulture', 'duck', 'crocodile', 'elephant', 'tiger'],
              'index': 2, 'coords': (0, 2) },
            { 'series': range(30, 50, 2),
              'index': 7, 'coords': (1, 0) },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                m.series, index, coords = config.values()
                new_index = m._fill(coords, index)
                self.assertIsInstance(new_index, int)
                self.assertEqual(new_index, index + 1)
                self.assertEqual(m.matrix[coords[0]][coords[1]],
                        m.series[index])

    def test_look(self):

        m = SpiralMatrix(self.matrix_dimension)

        pass_configs = [
            { 'cell': (1, 2), 'bearing': m.N, 'look': 'left',
              'want_cell': (1, 1) },
            { 'cell': (0, 0), 'bearing': m.E, 'look': 'right',
              'want_cell': (1, 0) },
            ### TODO: better handle a look outside the matrix. expect error?
            { 'cell': (0, 1), 'bearing': m.E, 'look': 'left',
              'want_cell': (-1, 1) },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                cell, bearing, look, want_cell = config.values()
                y, x = m._look(cell, look, bearing)
                self.assertEqual(y, want_cell[0])
                self.assertEqual(x, want_cell[1])

    def test_turn(self):

        m = SpiralMatrix(self.matrix_dimension)

        pass_configs = [
            { 'cell': (1, 1), 'turn': 'left', 'bearing': m.N,
              'want_bearing': m.W },
            { 'cell': (1, 0), 'turn': 'right', 'bearing': m.S,
              'want_bearing': m.W },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                cell, turn, bearing, want_bearing = config.values()
                new_bearing = m._turn(turn, bearing)
                self.assertEqual(new_bearing, want_bearing)

    def test_move(self):

        m = SpiralMatrix(self.matrix_dimension)

        pass_configs = [
            { 'cell': (1, 1), 'bearing': m.N,
              'want_cell': (0, 1) },
            { 'cell': (0, 2), 'bearing': m.S,
              'want_cell': (1, 2) },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                cell, bearing, want_cell = config.values()
                new_cell = m._move(cell, bearing)
                self.assertEqual(new_cell, want_cell)

class SpiralMatrixArgumentsTestCase(unittest.TestCase):

    def test_is_int(self):

        pass_configs = [-1, 1.0, 90, 1.2e6, '3']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertEqual(_is_int(config), int(config))

        fail_configs = [-0.01, 5.1, 1.2121e2, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(ArgumentError):
                    _is_int(config)

    def test_is_gt0(self):

        pass_configs = [2, 7.4, 17, 1.2121e2, '3']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertIs(_is_gt0(config), config)

        fail_configs = [-20, -0.0001, 0, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(ArgumentError):
                    _is_gt0(config)

    def test_is_not0(self):

        pass_configs = [-2, 0.901, 1.2121e2, 17, '3']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertIs(_is_not0(config), config)

        fail_configs = [0, 0.0, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(ArgumentError):
                    _is_not0(config)

    def test_is_odd_int(self):

        pass_configs = [-1, 1, 1.21e2, '3']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertIs(_is_odd_int(config), int(config))

        fail_configs = [-20, 0, 2.999, 1.2121e2, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(ArgumentError):
                    _is_odd_int(config)

    def test_is_not0_int(self):

        pass_configs = [-1, 4.0, 50]
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertIs(_is_not0_int(config), int(config))

        fail_configs = [-0, 0, 0.9, 1.2121e2, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(ArgumentError):
                    _is_not0_int(config)

    def test_is_gt0_odd_int(self):

        pass_configs = [1, 3.0, 55, '3']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertIs(_is_gt0_odd_int(config), int(config))

        fail_configs = [-2, 0, 6, 9.01, 1.2121e2, 'foo', '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(ArgumentError):
                    _is_gt0_odd_int(config)

    def test_is_bearing(self):

        pass_configs = ['e', 'S', 'WEST']
        for config in pass_configs:
            with self.subTest(config=config):
                self.assertEqual(_is_bearing(config), config.upper())

        fail_configs = ['foo', 'F', 12, '', None]
        for config in fail_configs:
            with self.subTest(config=config):
                with self.assertRaises(ArgumentError):
                    _is_bearing(config)

if __name__ == '__main__':
    unittest.main(verbosity=2)
