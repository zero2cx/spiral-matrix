#!/usr/bin/env python
# encoding: utf-8
# vim: set ff=unix fenc=utf-8 et ts=4 sts=4 sta sw=4:
#
# test_spiral_matrix.py

import unittest
from spiral_matrix.spiral_matrix import SpiralMatrix

################################################################################
class SpiralMatrixTestCase(unittest.TestCase):

    def test_01_simple_instantiation(self):

        pass_configs = [3, 5, 23, 1.21e2, '3']
        for config in pass_configs:
            with self.subTest(config=config):
                m = SpiralMatrix(config)
                self.assertIsInstance(m, SpiralMatrix)
                self.assertEqual(m.dimension, int(config))
                self.assertEqual(m.max, int(config) * int(config))

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
                dimension, bearing, right, start, step, file, words, \
                        want_matrix = config.values()
                m = SpiralMatrix(dimension, bearing, right, start, step, \
                        file, words, test=True)
                m._build()
                self.assertEqual(m.matrix, want_matrix)

################################################################################
class SpiralMatrixMethodsTestCase(unittest.TestCase):

    def test_01_series_from_integers(self):

        pass_configs = [
            { 'dimension': 5, 'start': 1, 'step': 1,
              'want_0_0_value': 17 },
            { 'dimension': 5, 'start': 1000, 'step': 2,
              'want_0_0_value': 1032 },
            { 'dimension': 5, 'start': -100, 'step': 3,
              'want_0_0_value': -52 },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                dimension, start, step, want_0_0_value = config.values()
                m = SpiralMatrix(dimension)
                m.series = m._series_from_integers(start, step)
                self.assertIsInstance(m.series, range)
                self.assertEqual(len(m.series), m.max)
                m._build()
                self.assertEqual(m.matrix[0][0], want_0_0_value)

    def test_02_series_from_string(self):

        pass_configs = [
            { 'dimension': 5, 'words': 'vulture duck crocodile elephant tiger',
              'want_0_0_value': 'duck' },
            { 'dimension': 5, 'words': '10 4 2 45 31 8.88 22 -7 0 94',
              'want_0_0_value': '22' },
            { 'dimension': 5, 'words': '~ @#$ ) ( !*% +!',
              'want_0_0_value': '!*%' },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                dimension, words, want_0_0_value = config.values()
                m = SpiralMatrix(dimension)
                m.series = m._series_from_string(words)
                self.assertIsInstance(m.series, list)
                self.assertEqual(len(m.series), m.max)
                m._build()
                self.assertEqual(m.matrix[0][0], want_0_0_value)

    def test_03_series_from_file(self):

        from os import path
        cwd = path.dirname(__file__)

        pass_configs = [
            { 'filename': f'{cwd}/test-input/3-letter-words.txt',
              'want_77th_element': 'cam' },
            { 'filename': f'{cwd}/test-input/5-letter-words.txt',
              'want_77th_element': 'cable' },
            { 'filename': f'{cwd}/test-input/lorem-ipsum.txt',
              'want_77th_element': 'Integer' },
        ]

        for config in pass_configs:
            with self.subTest(config=config):
                filename, want_77th_element = config.values()
                m = SpiralMatrix(9)
                series = m._series_from_file(filename)
                self.assertIsInstance(series, list)
                self.assertEqual(len(series), m.max)
                self.assertEqual(series[76], want_77th_element)

        fail_configs = [
            { 'filename': f'{cwd}/test-input/binary.dat' },
            { 'filename': f'{cwd}/test-input/empty.txt' },
        ]
        for config in fail_configs:
            with self.subTest(config=config):
                filename, = config.values()
                m = SpiralMatrix(3)
                with self.assertRaises(AttributeError):
                    series = m._series_from_file(filename)

    def test_04_width(self):

        pass_configs = [
            { 'series': ['vulture', 'duck', 'crocodile', 'elephant', 'tiger'],
              'want_width': 9 },
            { 'series': range(90, 110, 2),
              'want_width': 3 },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                series, want_width = config.values()
                m = SpiralMatrix(5)
                width = m._width(series)
                self.assertIsInstance(width, int)
                self.assertEqual(width, want_width)

    def test_05_fill(self):

        pass_configs = [
            { 'series': ['emu', 'duck', 'crocodile', 'shark', 'tiger', 'worm'],
              'index': 12,
              'want_coords': (1, 4) },
            { 'series': range(30, 50, 2),
              'index': 21,
              'want_coords': (4, 0) },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                series, index, want_coords = config.values()
                m = SpiralMatrix(5)
                m.series = (list(series) * 5)[:m.max]
                new_index = m._fill(want_coords, index)
                self.assertIsInstance(new_index, int)
                self.assertEqual(new_index, index + 1)
                self.assertEqual(m.series[index],
                        m.matrix[want_coords[0]][want_coords[1]])

    def test_06_look(self):

        pass_configs = [
            { 'cell': (1, 2), 'bearing': 'N', 'look': 'left',
              'want_cell': (1, 1) },
            { 'cell': (0, 0), 'bearing': 'E', 'look': 'right',
              'want_cell': (1, 0) },
            { 'cell': (0, 1), 'bearing': 'E', 'look': 'left',
              'want_cell': (-1, 1) },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                cell, bearing, look, want_cell = config.values()
                m = SpiralMatrix(5)
                bearing = m.compass[bearing]
                y, x = m._look(cell, look, bearing)
                self.assertEqual(y, want_cell[0])
                self.assertEqual(x, want_cell[1])

    def test_07_turn(self):

        pass_configs = [
            { 'cell': (1, 1), 'turn': 'left', 'bearing': 'N',
              'want_bearing': 'W' },
            { 'cell': (1, 0), 'turn': 'right', 'bearing': 'S',
              'want_bearing': 'W' },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                cell, turn, bearing, want_bearing = config.values()
                m = SpiralMatrix(5)
                bearing = m.compass[bearing]
                want_bearing = m.compass[want_bearing]
                new_bearing = m._turn(turn, bearing)
                self.assertEqual(new_bearing, want_bearing)

    def test_08_move(self):

        pass_configs = [
            { 'cell': (1, 1), 'bearing': 'N',
              'want_coords': (0, 1) },
            { 'cell': (0, 2), 'bearing': 'S',
              'want_coords': (1, 2) },
        ]
        for config in pass_configs:
            with self.subTest(config=config):
                cell, bearing, want_coords = config.values()
                m = SpiralMatrix(5)
                bearing = m.compass[bearing]
                y, x = m._move(cell, bearing)
                self.assertEqual((y, x), want_coords)

################################################################################
if __name__ == '__main__':
    unittest.main(verbosity=2)
