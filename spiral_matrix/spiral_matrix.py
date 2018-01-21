#!/usr/bin/env python
# encoding: utf-8
# vim: set ff=unix fenc=utf-8 et ts=4 sts=4 sta sw=4:
#
# spiral_matrix.py
# Build a square-shaped matrix with an outward-spiraling series of elements.
#
# Project home: <https://github.com/zero2cx/spiral-matrix>
# Copyright (C) 2018 David Schenck

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

################################################################################
class SpiralMatrix():
    '''
    Generate a square 2-d matrix with an outward-spiraling series of elements.

    A spiral matrix is a particular type of squared-shaped matrix where
    each cell is populated with one value from a series of elements. The
    'spiral' in 'spiral matrix' refers to the condition that each cell is
    progressively populated with a value from the series following a
    pattern that conforms to a tightly-wound spiral. This spiral
    progression begins from the center cell, moving outward. Ultimately,
    the entire matrix is populated with elements from the series.

    Column and row axis-labels along the top- and left-side can be
    prefixed to the printed output. Proceeding outward from the center
    cell in one compass direction or bearing, i.e East, North, West, or
    South, initiates the progression of the spiral. The spiral can be
    configured to progress in either a clockwise or counter-clockwise
    manner.

    The default style for the generated matrix consists of the series of
    integers that begin with '1' and then increments by '1' for each
    element of the series. Either of these integer values may be modified
    in order to change the generated matrix’s cell contents. Any positive
    or negative integer, or zero, is acceptable to occupy the center cell
    that starts the spiral. The increment integer must be a positive or
    negative, non-zero integer.

    As an alternative to populating the cells with a series of
    incrementing integers, a string of whitespace-delimited text
    elements, or word tokens, can be supplied. This string of tokens
    might consist of any combination of words, numbers, punctuation,
    or whitespace. The token string can be read from a file or stdin,
    or provided via command-line parameter.
    '''

    # The four compass-based vectors.
    N, W, S, E = (-1, 0), (0, -1), (1, 0), (0, 1)
    compass = {
        'E': E, 'EAST': E,
        'N': N, 'NORTH': N,
        'W': W, 'WEST': W,
        'S': S, 'SOUTH': S
    }

    # Map each compass-based vector to its relative-left and -right vector.
    vector = {
        'left': { E: N, N: W, W: S, S: E },
        'right': { E: S, S: W, W: N, N: E }
    }

    def __init__(self, dimension=None, bearing='E', turn=False,
            start=1, step=1, filename=None, words=None, testing=False):
        '''
        Generate a new instance of SpiralMatrix.

        Brief description of attributes:
            dimension : int : row- or column-count of the squared-shaped matrix
            origin    : y,x : grid coordinates of the center cell
            bearing   : E/N/W/S : initial compass bearing relative to the origin
            turn      : left/right : direction of the spiral progression
            max       : int : stop the progression-loop at this loop-count
            start     : int : numeric value populating the origin
            step      : int : incrementing step value of the numeric progression
            file      : file : named file containing space-delimited word tokens
            words     : str : string of space-delimited word tokens
            series    : list : list of elements with which to populate the cells
            width     : int : width of each matrix cell, in character-count
            test      : bool : only used when instantiated via test case
        '''

        # Assign attributes from arguments.
        self.dimension = self._dimension(dimension)
        self.origin = (self.dimension // 2, self.dimension // 2)
        self.max = self.dimension ** 2
        self.bearing = self._bearing(bearing)
        self.turn = 'right' if turn else 'left'
        self.series = self._series(
                filename, words, self._start(start), self._step(step))
        self.width = self._width(self.series)

        # Build the matrix structure that conforms to the attributes.
        if not testing:
            self._build()

    def _dimension(self, dimension):
        '''
        Raise exception, if dimension is not an odd, positive integer.

        Return dimension as type int().
        '''

        msg = f'not an odd, positive integer: "{dimension}"'

        try:
            dimension = int(dimension)
        except ValueError:
            raise AttributeError(msg)

        if not dimension > 0:
            raise AttributeError(msg)

        if not dimension % 2:
            raise AttributeError(msg)

        return dimension

    def _bearing(self, bearing):
        '''
        Raise exception, if bearing is not a key in the class compass dict().

        Return bearing as a 2-tuple of relative-to-position grid coordinates.
        '''

        msg = f'not a compass bearing: "{bearing}"'

        try:
            bearing = self.compass[bearing]
        except KeyError:
            raise AttributeError(msg)

        return bearing

    def _start(self, start):
        '''
        Raise exception, if start is not an integer.

        Return start as type int().
        '''

        msg = f'not an integer: "{start}"'

        try:
            start = int(start)
        except ValueError:
            raise AttributeError(msg)

        return start

    def _step(self, step):
        '''
        Raise exception, if step is not a non-zero integer.

        Return step as type int().
        '''

        msg = f'not a non-zero integer: "{step}"'

        try:
            step = int(step)
        except ValueError:
            raise AttributeError(msg)

        if step == 0:
            raise AttributeError(msg)

        return step

    def _series(self, filename, words, start, step):
        '''
        Populate series via file content, word tokens, or range of integers.

        Return series as a list() or a range().
        '''

        if filename:
            return self._series_from_file(filename)

        if words:
            return self._series_from_string(words)

        return self._series_from_integers(start, step)

    def _series_from_file(self, filename):
        '''
        Populate series using text from a local file.

        Raise exception, if the file is binary or is empty text.
        Return the series list.
        '''

        max = self.max

        try:
            with open(filename) as file:
                series = file.read()
        except UnicodeDecodeError:
            msg = f'"{filename}": not a text file'
            raise AttributeError(msg)

        try:
            series = series.split()
            series = (series * (int(max / len(series)) + 1))[:max]
        except:
            msg = f'"{filename}": empty file found'
            raise AttributeError(msg)

        return series

    def _series_from_string(self, words):
        '''
        Populate series using a space-delimited string to fill the matrix cells.

        Return the series list.
        '''

        max = self.max

        series = words.split()
        series = (series * (int(max / len(series)) + 1))[:max]

        return series

    def _series_from_integers(self, start, step):
        '''
        Populate series with integer values to fill the matrix cells.

        Return the series list.
        '''

        max = self.max

        try:
            series = range(start, start + max * step, step)[:max]
        except IndexError:
            msg = f'start:{start}  step:{step}  max:{max}  end:{start+max*step}'
            raise AttributeError(msg)

        return series

    def _width(self, series):
        '''
        Set cell-width for printing, equal to the widest element in the series.

        Return the width integer.
        '''

        width = 0
        for i in range(len(series)):
            if len(str(series[i])) > width:
                width = len(str(series[i]))

        return width

    def _fill(self, coords, index):
        '''
        Populate the current cell with the currently indexed element of series.

        Increment the series index integer and return that index.
        '''

        y, x = coords

        self.matrix[y][x] = self.series[index]

        return index + 1

    def _look(self, location, look, bearing):
        '''
        Determine cell coords of relative-left/right cell from the current cell.

        Return the cell coordinates tuple.
        '''

        vector = self.vector[look][bearing]

        return [sum(coords) for coords in zip(location, vector)]

    def _turn(self, turn, bearing):
        '''
        Turn towards the left- or right-adjacent cell, relative to current.

        Return 2-tuple of the new compass bearing.
        '''

        return self.vector[turn][bearing]

    def _move(self, cell, bearing):
        '''
        Move forward one cell.

        Return 2-tuple of coordinates for the new current cell.
        '''

        return tuple([sum(coords) for coords in zip(cell, bearing)])

    def _build(self):
        '''
        Generate the spiral matrix, populating it with elements of series.
        '''

        dimension = self.dimension
        cell = self.origin
        bearing = self.bearing
        turn = self.turn
        max = self.max
        index = 0

        # Generate an empty list-of-lists, populate the cells with 'None'.
        self.matrix = []
        for i in range(dimension):
            self.matrix.append([None] * dimension)

        # Start in the origin cell and spiral outward.
        # Populate each cell with the next element of series.
        index = self._fill(cell, index)                         # fill
        cell = self._move(cell, bearing)                        # move
        while index < max:
            index = self._fill(cell, index)                     # fill
            y, x = self._look(cell, turn, bearing)              # look
            if self.matrix[y][x] == None:                       # can turn?
                bearing = self._turn(turn, bearing)             #   turn
            cell = self._move(cell, bearing)                    # move

    def show(self, axes=False):
        '''
        Print the 2-d matrix structure.
        '''

        # Print column-labels across the top, if needed.
        if axes:
            print('    ', end='')
            for n in range(self.dimension):
                print('%*s ' % (self.width, n), end='')
            print()

        # Print the matrix structure.
        # Prefix a row-label before each row, if needed.
        for i in range(self.dimension):
            if axes:
                print('%2s  ' % (i), end='')
            for j in range(self.dimension):
                print('%*s ' % (self.width, self.matrix[i][j]), end='')
            print()

################################################################################
def main():
    '''
    Handle the case where this module is launched from the command-line.
    '''

    from sys import stdin
    from command_line import CommandLineInterface

    # Parse command-line arguments and stdin.
    # Print usage help, if needed.
    cli = CommandLineInterface(SpiralMatrix)
    args = cli.parser.parse_args()
    if args.words == None:
        args.words = stdin.read()

    # Instantiate and print the spiral matrix.
    m = SpiralMatrix(dimension=args.DIMENSION, bearing=args.bearing,
                turn=args.right, start=args.center, step=args.step,
                filename=args.file, words=args.words)
    m.show(axes=args.axes)

if __name__ == '__main__':
    main()
