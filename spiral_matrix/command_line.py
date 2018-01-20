#!/usr/bin/env python
# encoding: utf-8
# vim: set ff=unix fenc=utf-8 et ts=4 sts=4 sta sw=4:
#
# command_line.py
# Configure the command-line interface for the spiral_matrix module.
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

import argparse

################################################################################
class CommandLineInterface():

    def __init__(self, caller):

        self.caller = caller
        self.parser = self.configure_parser()

    def configure_parser(self):
        '''
        Configure the parser to process the command-line arguments.

        The parser will quit and print a help message in response to incoherent
        argument usage.
        '''
        parser = argparse.ArgumentParser(
                description=self.caller.__doc__,
                formatter_class=argparse.RawDescriptionHelpFormatter)

        # arg: DIMENSION
        parser.add_argument(
                'DIMENSION',
                type=self.arg_is_gt0_odd_int,
                help='This is an integer argument, and is limited '
                'to odd numbers only. This count of rows and columns '
                'constitute the constructed size of the the square-'
                'shaped 2-d matrix. (REQUIRED)')

        # arg: axes
        parser.add_argument(
                '-a', '--axes',
                action='store_true',
                default=False,
                help='This parameter-less option enables or disables the '
                'prefixing of column- and row-axes labels along the '
                'top- and left-side of the printed output. '
                '(default: False)')

        # arg: bearing
        parser.add_argument(
                '-b', '--bearing',
                type=self.arg_is_bearing,
                default='E',
                help='This compass bearing (N, E, S, or W) specifies '
                'the direction that is used to proceed initially '
                'outward from the center of the matrix. '
                '(default: E)')

        turn_group = parser.add_mutually_exclusive_group()

        # arg: right
        turn_group.add_argument(
                '-r', '--right',
                action='store_true',
                default=False,
                help='This parameter-less option generates a spiral '
                'which progresses in a clockwise manner. Not for use '
                'with \'left\'. (default: not used)')

        # arg: left
        turn_group.add_argument(
                '-l', '--left',
                action='store_true',
                default=True,
                help='This parameter-less option generates a spiral '
                'which progresses in a counter-clockwise manner, '
                'which is the default spiral direction. Not for use '
                'with \'right\'. Included for completeness.')

        default_group = parser.add_argument_group(
                'Integer-filled matrix options',
                'Matrix cells are filled with incrementing integers, by '
                'default.')

        # arg: center
        default_group.add_argument(
                '-c', '--center',
                type=int,
                default=1,
                help='This integer argument is used to populate the center '
                'cell that begins the spiral. (default: 1)')

        # arg: step
        default_group.add_argument(
                '-s', '--step',
                type=self.arg_is_not0_int,
                default=1,
                help='This integer argument is used to increment the next '
                'cell\'s value as the spiral progresses from cell to '
                'cell. (default: 1)')

        alternative_group = parser.add_argument_group(
                'Token-filled matrix options',
                'Alternatively, matrix cells can be populated with specified '
                'text elements.')
        alternative_subgroup = alternative_group.add_mutually_exclusive_group()

        # arg: file
        alternative_subgroup.add_argument(
                '-f', '--file',
                # type=open,
                type=self.arg_is_text_file,
                help='The specified file should contain some amount of '
                'whitespace-delimited text elements. The cells of '
                'the matrix are then populated using these elements. '
                'Usage of the \'words\' option is excluded when using '
                'this option. (default: not used)')

        # arg: words
        alternative_subgroup.add_argument(
                '-w', '--words',
                type=str,
                nargs='?',
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

    def arg_is_odd_int(self, arg):
        '''
        Argument contraint: odd integer
        '''
        msg = f'"{arg}" should be an odd integer'

        # test: is arg an integer?
        try:
            int(arg)
        except:
            raise argparse.ArgumentTypeError(msg)

        # test: is arg an integer after being coerced to type float?
        if not float(arg).is_integer():
            raise argparse.ArgumentTypeError(msg)

        # test: is arg evenly divisible by 2?
        if not int(arg) % 2:
            raise argparse.ArgumentTypeError(msg)

        return arg

    def arg_is_not0_int(self, arg):
        '''
        Argument contraint: non-zero integer
        '''
        msg = f'"{arg}" should be a non-zero integer'

        # test: is arg an integer?
        try:
            int(arg)
        except:
            raise argparse.ArgumentTypeError(msg)

        # test: is arg an integer after being coerced to type float?
        if not float(arg).is_integer():
            raise argparse.ArgumentTypeError(msg)

        # test: is arg equal to 0?
        if int(arg) == 0:
            raise argparse.ArgumentTypeError(msg)

        return arg

    def arg_is_gt0_odd_int(self, arg):
        '''
        Argument contraint: positive, odd integer
        '''
        msg = f'"{arg}" should be a positive, odd integer'

        # test: is arg an integer?
        try:
            int(arg)
        except:
            raise argparse.ArgumentTypeError(msg)

        # test: is arg an integer after being coerced to type float?
        if not float(arg).is_integer():
            raise argparse.ArgumentTypeError(msg)

        # test: is arg evenly divisible by 2?
        if not int(arg) % 2:
            raise argparse.ArgumentTypeError(msg)

        # test: is arg greater than 0?
        if int(arg) <= 0:
            raise argparse.ArgumentTypeError(msg)

        return arg

    def arg_is_bearing(self, arg):
        '''
        Argument contraint: valid compass bearing as defined by self.caller
        '''
        bearing_list = list(self.caller.compass.keys())
        msg = f'"{arg}" should be one of: {bearing_list}'

        # test: is arg a member of bearing_list?
        if not str(arg).upper() in bearing_list:
            raise argparse.ArgumentTypeError(msg)

        return arg

    def arg_is_text_file(self, arg):
        '''
        Argument contraint: text file
        '''

        msg = f'{arg} should be a text file'

        # test: is file readable as text?
        try:
            with open(arg) as file:
                file.read()
        except UnicodeDecodeError:
            raise argparse.ArgumentTypeError(msg)

        return arg

################################################################################
if __name__ == '__main__':
    pass
