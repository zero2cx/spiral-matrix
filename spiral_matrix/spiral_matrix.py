#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# spiral_matrix.py

# Build a square-shaped matrix with an outward-spiraling series of elements.
#   Project home: <https://github.com/zero2cx/spiral-matrix>
#   Copyright (C) 2018 David Schenck
#
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

class SpiralMatrix():
    '''
    Construct a square 2-d matrix with an outward-spiraling series of elements.

    The series of elements that fill the matrix's cells consists of a sequence
    of incrementing integers, by default. The initial integer may be specified,
    as well as the increment value. Any positive or negative integer, or zero,
    is allowed for the initial integer value. The value of the increment must
    be a non-zero integer.

    The spiral can progress in either a clockwise or counter-clockwise manner.
    Proceeding outward from the center-cell in one compass direction, i.e East,
    North, West, or South, initiates the progression of the spiral. When
    printing to the console, column and row axis-labels along the top- and left-
    side can be prefixed to the output.

    As an alternative to the population of the cells of the matrix with a
    progression of incrementing integers, a string of space-delimited text
    elements can be supplied. This string of elements might consist of any
    combination of words, numbers, punctuation, or whitespace. The text elements
    will be read from a file or stdin, or provided via the command-line.
    '''
    '''The four compass-based vectors.'''
    N, W, S, E = (-1, 0), (0, -1), (1, 0), (0, 1)
    compass = {
        'E': E, 'EAST': E,
        'N': N, 'NORTH': N,
        'W': W, 'WEST': W,
        'S': S, 'SOUTH': S
    }
    '''Map the compass-based vectors to relative-left and -right vectors.'''
    vector = {
        'left': { E: N, N: W, W: S, S: E },
        'right': { E: S, S: W, W: N, N: E }
    }

    def __init__(self, dimension=None, right=False, bearing='E', start=1,
            step=1, file=None, words=None):
        '''
        Create a new instance of a 2-d spiral matrix.

        Description of instance attributes:
            dimension : int : row- and column-count of the matrix
            turn      : left/right : direction of the spiral progression
            bearing   : E/N/W/S : initial compass bearing
            start     : int : numeric value inside the origin cell
            step      : int : increment-step of a numeric progression
            origin    : y,x : coordinates of the center cell
            max       : int : stop the progression-loop at this loop-count
            file      : file : named file containing space-delimited elements
            words     : str : string of space-delimited elements
            series    : list : list of elements with which to fill the cells
            width     : int : width of one cell, in character-count
        '''
        try:
            self.dimension = int(dimension) if int(dimension) else 'invalid'
            self.turn = 'right' if right else 'left'
            self.bearing = self.compass[bearing]
            self.start = start
            self.step = step
            self.origin = (int(self.dimension // 2), int(self.dimension // 2))
            self.max = self.dimension ** 2
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
        '''Build the matrix that conforms to the instance attributes.'''
        self._build()

    def _series(self):
        '''
        Populate the series of values that will fill the matrix cells.
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
        Populate series using a string to fill the matrix cells.
        '''
        words = self.words
        max = self.max
        series = words.split()
        series = (series * (int(max / len(series)) + 1))[:max]
        return series

    def _width(self):
        '''
        Set cell-width for printing, equal to the widest element in the series.
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

        Return an incremented series index-counter.
        '''
        y, x = coords
        try:
            self.matrix[y][x] = self.series[index]
        except IndexError:
            return index + 1
        return index + 1

    def _look(self, location, look, bearing):
        '''
        Determine the coords of the cell to the left/right of the current cell.

        Return the coords of that cell.
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
        Return the new bearing that points directly to the left or right.
        '''
        return self.vector[turn][bearing]

    def _move(self, cell, bearing):
        '''
        Move forward one cell, returning coordinates for the new current cell.
        '''
        return tuple([sum(coords) for coords in zip(cell, bearing)])

    def _build(self):
        '''
        Populate the spiral matrix with a progressing series of elements.
        '''
        dimension = self.dimension
        cell = self.origin
        bearing = self.bearing
        turn = self.turn
        index = 0
        max = self.max
        '''Generate a 2-d matrix and populate the cells with 'None'.'''
        self.matrix = []
        for i in range(dimension):
            self.matrix.append([None] * dimension)
        '''Start in the origin cell and spiral outward, filling each cell
        as the spiral progresses.'''
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
        Print the 2-d matrix with the column and row axes labelled, or without.
        '''
        '''Print column-labels along the top, or not.'''
        if axes:
            print('    ', end='')
            for n in range(self.dimension):
                print('%*s ' % (self.width, n), end='')
            print()
        '''Print the matrix. Include row-labels along the left side, or not.'''
        for i in range(self.dimension):
            if axes:
                print('%2s  ' % (i), end='')
            for j in range(self.dimension):
                print('%*s ' % (self.width, self.matrix[i][j]), end='')
            print()

################################################################################
class ArgumentError(Exception):
    pass

################################################################################
def _is_int(value):
    '''
    Argument contraint: integer value
    '''
    msg = '\'%s\' should be an integer value' % (str(value))
    if value == None:
        raise ArgumentError(msg)
    try:
        integer = int(value)
    except ValueError:
        raise ArgumentError(msg)
    if not float(value).is_integer():
        raise ArgumentError(msg)
    return integer

def _is_gt0(value):
    '''
    Argument contraint: greater-than-zero numeric value
    '''
    msg = '\'%s\' should be a greater-than-zero numeric value' % (str(value))
    try:
        float(value)
    except:
        raise ArgumentError(msg)
    if float(value) <= 0:
        raise ArgumentError(msg)
    return value

def _is_not0(value):
    '''
    Argument contraint: non-zero numeric value
    '''
    msg = '\'%s\' should be a non-zero numeric value' % (str(value))
    try:
        float(value)
    except:
        raise ArgumentError(msg)
    if value == 0:
        raise ArgumentError(msg)
    return value

def _is_odd_int(value):
    '''
    Argument contraint: odd integer value
    '''
    msg = '\'%s\' should be an odd integer value' % (str(value))
    try:
        integer = _is_int(value)
    except:
        raise ArgumentError(msg)
    if not integer % 2:
        raise ArgumentError(msg)
    return integer

def _is_not0_int(value):
    '''
    Argument contraint: non-zero integer value
    '''
    msg = '\'%s\' should be a non-zero integer value' % (str(value))
    try:
        integer = _is_int(value)
        integer = _is_not0(integer)
    except:
        raise ArgumentError(msg)
    return integer

def _is_gt0_odd_int(value):
    '''
    Argument contraint: positive, odd integer value
    '''
    msg = '\'%s\' should be a positive, odd integer value' % (str(value))
    try:
        integer = _is_odd_int(value)
        integer = _is_gt0(integer)
    except:
        raise ArgumentError(msg)
    return integer

def _is_bearing(value):
    '''
    Argument contraint: valid compass bearing as defined by SpiralMatrix
    '''
    uppercase_value = str(value).upper()
    bearing_list = list(SpiralMatrix.compass.keys())
    msg = '\'%s\' should be one of: %s' % (str(value), bearing_list)
    if not uppercase_value in bearing_list:
        raise ArgumentError(msg)
    return uppercase_value

def _configure_parser():
    '''
    Configure the parser to process the command-line arguments.

    The parser will quit and print a help message in response to incoherent
    argument usage.
    '''
    parser = argparse.ArgumentParser(description=SpiralMatrix.__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('DIMENSION', type=_is_gt0_odd_int,
            help='This parameter is an integer value, and is limited '
            'to odd numbers only. This count of rows and columns '
            'constitute the constructed size of the the square-'
            'shaped 2-d matrix. (REQUIRED)')
    parser.add_argument('-a', '--axes', action='store_true',
            default=False,
            help='Useful when printing the matrix to the console. '
            'This parameter-less option will include column- '
            'and row-axes labels along the top- and left-side. '
            '(default: not used)')
    spiral_group = parser.add_mutually_exclusive_group()
    spiral_group.add_argument('-r', '--right', action='store_true',
            default=False,
            help='This parameter-less option constructs a spiral '
            'which progresses in a clockwise manner. Not for use '
            'with \'left\'. (default: not used)')
    spiral_group.add_argument('-l', '--left', action='store_true',
            default=True,
            help='This parameter-less option constructs a spiral '
            'which progresses in a counter-clockwise manner, '
            'which is the default spiral direction. Not for use '
            'with \'right\'. Included for completeness.')
    parser.add_argument('-b','--bearing', type=_is_bearing,
            default='E',
            help='This compass bearing (N, E, S, or W) specifies '
            'the direction used to proceed initially outward '
            'from the center of the matrix. (default: E)')
    integers_group = parser.add_argument_group('Integer-filled matrix options',
            'Matrix cells are filled with incrementing integers, by default.')
    integers_group.add_argument('-c', '--center', type=int,
            default=1,
            help='This integer value is used to populate the center '
            'cell. (default: 1)')
    integers_group.add_argument('-s', '--step', type=_is_not0_int,
            default=1,
            help='This integer value is used to increment the next '
            'cell\'s value as the spiral progresses from cell to '
            'cell. (default: 1)')
    group_words = parser.add_argument_group('Word-filled matrix options',
            'Alternatively, matrix cells can be populated with supplied text '
            'elements.')
    words_group = group_words.add_mutually_exclusive_group()
    words_group.add_argument('-f', '--file', type=open,
            help='The specified file should contain some amount of '
            'whitespace-delimited text elements. The cells of '
            'the matrix are then populated using these elements. '
            'Usage of the \'words\' option is excluded when using '
            'this option. (default: not used)')
    words_group.add_argument('-w', '--words', type=str, nargs='?',
            default=False,
            help='This string of whitespace-delimited text elements '
            'is used to populate the cells of the matrix. When '
            'this option is present with no string parameter '
            'given, then string is read from stdin. When '
            'utilizing stdin, this option needs to be the last '
            'option provided on the command-line. Usage of the '
            '\'file\' option is excluded when using this option. '
            '(default: not used)')
    return parser

def main():
    '''
    Handle the case where this module is launched from the command-line.
    '''
    '''Parse the command-line arguments. Usage help is printed, if necessary.'''
    parser = _configure_parser()
    args = parser.parse_args()
    if args.words == None:
        args.words = sys.stdin.read()
    '''Build and print the spiral matrix using the parsed arguments.'''
    try:
        m = SpiralMatrix(dimension=args.DIMENSION, right=args.right,
                bearing=args.bearing, start=args.center, step=args.step,
                file=args.file, words=args.words)
    except AttributeError:
        sys.exit('** AttributeError: %s\n   Attributes List: %s' % (
                'could not instantiate SpiralMatrix',
                str(vars(args)).strip('{}')))
    m.show(args.axes)

if __name__ == '__main__':
    import sys
    import argparse
    main()
