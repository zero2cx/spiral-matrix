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

    A spiral matrix is a particular type of squared-shaped matrix where each
    cell is populated with a progression of elements of a series. The spiral in
    the name refers to the condition that the cells are filled using a pattern
    that conforms to a tightly-wound spiral. The spiral progression begins in
    the center cell. From there, the progression spirals outward moving from
    cell to cell, filling each one with an element of the series. Ultimately,
    each cell in the matrix is populated with one element of the series.

    Column and row axis-labels along the top- and left-side can be prefixed to
    the printed output. Proceeding outward from the center cell in one compass
    direction or bearing, i.e East, North, West, or South, initiates the
    progression of the spiral. The spiral can progress in either a clockwise or
    counter-clockwise manner.

    The default style for the generated matrix consists of the series of
    integers that begin with 1 and then increments by 1 for each member of the
    series. Either of these integer values may be modified in order to change
    the generated matrix's cell contents. Any positive or negative integer, or
    zero, is acceptable to occupy the center cell that begins the spiral. The
    increment integer must be a positive or negative, non-zero integer.

    As an alternative to the population of the cells of the matrix with the
    series of incrementing integers, a string of whitespace-delimited text
    elements can be supplied. This string of elements might consist of any
    combination of words, numbers, punctuation, or whitespace. The text
    elements will be read from a file or stdin, or provided in a string via
    the command-line.
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
            start=1, step=1, file=None, words=None, test=False):
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
        try:
            self.dimension = int(dimension) if int(dimension) else 'invalid'
            self.origin = (int(self.dimension // 2), int(self.dimension // 2))
            self.bearing = self.compass[bearing]
            self.turn = 'right' if turn else 'left'
            self.max = self.dimension ** 2
            self.start = start
            self.step = step
            self.file = file
            self.words = words
            if self.file:
                self.series = self._series_from_file()
            elif self.words:
                self.series = self._series_from_string()
            else:
                self.series = self._series()
            self.width = self._width()
        except:
            raise AttributeError
        # Build the matrix structure that conforms to the attributes.
        if not test:
            self._build()

    def _series(self):
        '''
        Populate series with integer values to fill the matrix cells.

        Return the series list.
        '''
        start = self.start
        step = self.step
        max = self.max
        try:
            ### TODO: tweak the clumsy end-of-range expression below
            series = range(start, (max + abs(start)) * step, step)[:max]
        except IndexError:
            raise AttributeError
        return series

    def _series_from_file(self):
        '''
        Populate series using content of a local file to fill the matrix cells.

        Return the series list.
        '''
        file = self.file
        max = self.max
        ### TODO: use the try-except here to catch an empty file or binary file
        try:
            series = file.read()
            series = series.split()
            series = (series * (int(max / len(series)) + 1))[:max]
        except:
            raise AttributeError
        return series

    def _series_from_string(self):
        '''
        Populate series using a space-delimited string to fill the matrix cells.

        Return the series list.
        '''
        words = self.words
        max = self.max
        series = words.split()
        series = (series * (int(max / len(series)) + 1))[:max]
        return series

    def _width(self):
        '''
        Set cell-width for printing, equal to the widest element in the series.

        Return the width integer.
        '''
        series = self.series
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
        try:
            self.matrix[y][x] = self.series[index]
        except IndexError:
            return index + 1
        return index + 1

    def _look(self, location, look, bearing):
        '''
        Determine cell coords of relative-left/right cell from the current cell.

        Return the cell coordinates tuple.
        '''
        vector = self.vector[look][bearing]
        y, x = [sum(coords) for coords in zip(location, vector)]
        try:
            self.matrix[y][x]
        except IndexError:
            raise AttributeError
        return y, x

    def _turn(self, turn, bearing):
        '''
        Turn towards the left- or right-adjacent cell, relative to current.

        Return the compass bearing of the new direction.
        '''
        return self.vector[turn][bearing]

    def _move(self, cell, bearing):
        '''
        Move forward one cell.

        Return coordinates tuple for the new current cell.
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
        index = 0
        max = self.max
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
    # Build and print the spiral matrix using the parsed command-line args.
    try:
        m = SpiralMatrix(dimension=args.DIMENSION, bearing=args.bearing,
                turn=args.right, start=args.center, step=args.step,
                file=args.file, words=args.words).show(axes=args.axes)
    except AttributeError:
        print('** AttributeError: %s\n   Attributes List: %s' % (
                'could not instantiate SpiralMatrix',
                str(vars(args)).strip('{}')))

if __name__ == '__main__':
    main()
