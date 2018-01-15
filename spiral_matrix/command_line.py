#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# command_line.py

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
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

import argparse

################################################################################
class ArgumentError(Exception):
    pass

################################################################################
class CommandLineInterface():

    def __init__(self):
        pass

    def arg_is_int(self, value):
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

    def arg_is_gt0(self, value):
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

    def arg_is_not0(self, value):
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

    def arg_is_odd_int(self, value):
        '''
        Argument contraint: odd integer value
        '''
        msg = '\'%s\' should be an odd integer value' % (str(value))
        try:
            integer = self.arg_is_int(value)
        except:
            raise ArgumentError(msg)
        if not integer % 2:
            raise ArgumentError(msg)
        return integer

    def arg_is_not0_int(self, value):
        '''
        Argument contraint: non-zero integer value
        '''
        msg = '\'%s\' should be a non-zero integer value' % (str(value))
        try:
            integer = self.arg_is_int(value)
            integer = self.arg_is_not0(integer)
        except:
            raise ArgumentError(msg)
        return integer

    def arg_is_gt0_odd_int(self, value):
        '''
        Argument contraint: positive, odd integer value
        '''
        msg = '\'%s\' should be a positive, odd integer value' % (str(value))
        try:
            integer = self.arg_is_odd_int(value)
            integer = self.arg_is_gt0(integer)
        except:
            raise ArgumentError(msg)
        return integer

    def arg_is_bearing(self, value):
        '''
        Argument contraint: valid compass bearing as defined by SpiralMatrix
        '''
        uppercase_value = str(value).upper()
        # bearing_list = list(SpiralMatrix.compass.keys())
        bearing_list = ['E', 'N', 'W', 'S']
        msg = '\'%s\' should be one of: %s' % (str(value), bearing_list)
        if not uppercase_value in bearing_list:
            raise ArgumentError(msg)
        return uppercase_value

    def configure_parser(self, description='DESCRIPTION HERE'):
        '''
        Configure the parser to process the command-line arguments.

        The parser will quit and print a help message in response to incoherent
        argument usage.
        '''
        dim = [
            [('DIMENSION', ), ('type', 'cli.arg_is_gt0_odd_int'),
             ('help', 'This parameter is an integer value, and is limited '
                      'to odd numbers only. This count of rows and columns '
                      'constitute the constructed size of the the square-'
                      'shaped 2-d matrix. (REQUIRED)')
            ]
        ]
        cli = CommandLineInterface()
        parser = argparse.ArgumentParser(description=description,
                formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('DIMENSION', type=cli.arg_is_gt0_odd_int,
                help='This parameter is an integer value, and is limited '
                'to odd numbers only. This count of rows and columns '
                'constitute the constructed size of the the square-'
                'shaped 2-d matrix. (REQUIRED)')
        parser.add_argument('-a', '--axes', action='store_true',
                default=False,
                help='This parameter-less option enables or disables the '
                'prefixing of column- and row-axes labels along the '
                'top- and left-side of the printed output. '
                '(default: False)')
        parser.add_argument('-b','--bearing', type=cli.arg_is_bearing,
                default='E',
                help='This compass bearing (N, E, S, or W) specifies '
                'the direction that is used to proceed initially '
                'outward from the center of the matrix. '
                '(default: E)')
        spiral_group = parser.add_mutually_exclusive_group()
        spiral_group.add_argument('-r', '--right', action='store_true',
                default=False,
                help='This parameter-less option generates a spiral '
                'which progresses in a clockwise manner. Not for use '
                'with \'left\'. (default: not used)')
        spiral_group.add_argument('-l', '--left', action='store_true',
                default=True,
                help='This parameter-less option generates a spiral '
                'which progresses in a counter-clockwise manner, '
                'which is the default spiral direction. Not for use '
                'with \'right\'. Included for completeness.')
        integers_group = parser.add_argument_group('Integer-filled matrix options',
                'Matrix cells are filled with incrementing integers, by default.')
        integers_group.add_argument('-c', '--center', type=int,
                default=1,
                help='This integer value is used to populate the center '
                'cell that begins the spiral. (default: 1)')
        integers_group.add_argument('-s', '--step', type=cli.arg_is_not0_int,
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
                'utilizing stdin for string input, this option needs '
                'to be the last option provided on the command-line. '
                'Usage of the \'file\' option is excluded when using '
                'this option. (default: not used)')
        return parser

################################################################################
if __name__ == '__main__':
    pass
