#!/usr/bin/env python
# encoding: utf-8
# vim: set ff=unix fenc=utf-8 et ts=4 sts=4 sta sw=4:
#
# test_spiral_matrix.py

import unittest
from spiral_matrix.spiral_matrix import SpiralMatrix

################################################################################
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
            { 'dimension': 5, 'bearing': 'E', 'right': False, 'start': 1,
              'step': 1, 'file': None, 'words': None,
              'want_matrix': [[17, 16, 15, 14, 13],
                              [18,  5,  4,  3, 12],
                              [19,  6,  1,  2, 11],
                              [20,  7,  8,  9, 10],
                              [21, 22, 23, 24, 25]] },
            { 'dimension': 3, 'bearing': 'N', 'right': True, 'start': 1,
              'step': 1, 'file': None,
              'words': 'eenie meenie minie moe',
              'want_matrix': [['eenie', 'meenie', 'minie'],
                              [  'moe',  'eenie',   'moe'],
                              ['minie', 'meenie', 'eenie']] },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                dimension, turn, bearing, start, step, file, words, \
                        want_matrix = config.values()
                m = SpiralMatrix(dimension, turn, bearing, start, step, file, \
                        words)
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
                m.start, m.step, want_0_0_value = config.values()
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
                m.words, want_0_0_value = config.values()
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
                filename, want_0_0_value = config.values()
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
        #             with self.assertRaises(argparse.ArgumentError):
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

################################################################################
if __name__ == '__main__':
    unittest.main(verbosity=2)
