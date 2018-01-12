============
SpiralMatrix
============

-----------------------------------------------------------------------------
Construct a square 2-d matrix with an outward-spiraling series of elements.
-----------------------------------------------------------------------------

.. image:: docs/images/spiral_matrix_5.png
   :alt: 5x5

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
The individual customizable features of SpiralMatrix are detailed below.

**Required parameter:**

    DIMENSION
        This parameter is an integer value, and is limited
        to odd numbers only. This count of rows and columns
        constitute the constructed size of the the square-
        shaped 2-d matrix. (REQUIRED)

.. image:: docs/images/spiral_matrix_5+command_line.png
   :alt: 5x5 with command-line

**General-purpose options:**

    --axes
        Useful when printing the matrix to the console.
        This parameter-less option will include column-
        and row-axes labels along the top- and left-side.
        (default: not used)
    --right
        This parameter-less option constructs a spiral
        which progresses in a clockwise manner. Not for use
        with 'left'. (default: not used)
    --left
        This parameter-less option constructs a spiral
        which progresses in a counter-clockwise manner,
        which is the default spiral direction. Not for use
        with 'right'. Included for completeness.
    --bearing EAST | NORTH | WEST | SOUTH
        This compass bearing (E, N, W, or S) specifies
        the direction used to proceed initially outward
        from the center of the matrix. (default: E)

.. image:: docs/images/spiral_matrix_7+axes+bearing_south+center1000+step-300.png
   :alt: 7x7 with axes, bearing south, center 1000, step -300

**Options for integer-populated matrix cells.** Matrix cells are
populated with incrementing integer values, by default. Use of the
following options will modify the implementation of that default
behavior.

    --center INTEGER
        This integer value is used to populate the center
        cell. (default: 1)
    --step INTEGER
        This integer value is used to increment the next
        cell's value as the spiral progresses from cell to
        cell. (default: 1)

**Options for text element-populated matrix cells.** Alternatively, matrix
cells can be populated with supplied text elements. Use of either of
the following options replaces the default behavior described above.

    --file FILENAME
        The specified file should contain some amount of
        whitespace-delimited text elements. The cells of
        the matrix are then populated using these elements.
        Usage of the 'words' option is excluded when using
        this option. (default: not used)
    --words [STRING]
        This string of whitespace-delimited text elements
        is used to populate the cells of the matrix. When
        this option is present with no string parameter
        given, then string is read from stdin. When
        utilizing stdin, this option needs to be the last
        option provided on the command-line. Usage of the
        'file' option is excluded when using this option.
        (default: not used)

.. image:: docs/images/spiral_matrix_5+axes+bearing_south+right+file_lorem_ipsum.png
   :alt: 5x5 cells with axes, bearing south, lorem_ipsum.txt
.. image:: docs/images/spiral_matrix_9+right+words_stormy_night.png
   :width: 900
   :alt: 9x9, right, stormy_night

:License: GPL3+
:Document version: 1.0
:Modified: 01/11/2018
:Author: David Schenck
