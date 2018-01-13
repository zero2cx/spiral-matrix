# SpiralMatrix

## Construct a square 2-d matrix with an outward-spiraling series of elements


A matrix in the context of this code module is an array whose membership is made
up of a number of other arrays that are all uniform in size. This array-of-
arrays construct thus forms a two-dimensional grid made up of individual cells.

![5x5 spiral matrix](docs/images/spiral_matrix_5.png "5x5 spiral matrix")

A spiral matrix is a particular type of squared-shaped matrix where each cell is
populated with one element taken from a specified series of elements. The spiral
in the name originates from the condition that all cells are filled utilizing a
pattern that conforms to a tightly-wound spiral. The cell-to-cell spiral
progression begins in the center cell. From there, the progression spirals ever-
outward, moving from cell to cell filling each with an element of the series.
Ultimately, each cell in the matrix is populated with one element from that
series of elements.

![5x5 including command-line](docs/images/spiral_matrix_5+command_line.png "5x5  including command-line")

This remainder of this document details the functionality of executing the
SpiralMatrix from the command-line. For documentation on usage of SpiralMatrix
when importing the code as a python module, please [click here](./docs/SpiralMatrix.md "The Spiral Matrix module API").

#### Required parameter

    DIMENSION
        This parameter is an integer value, and is limited
        to odd numbers only. This count of rows and columns
        constitute the constructed size of the the square-
        shaped 2-d matrix. (REQUIRED)

#### General-purpose options

When printing to the console, column and row axis-labels along the top- and
left-side can be prefixed to the output. The spiral can progress in either
a clockwise or counter-clockwise manner. Proceeding outward from the
center-cell in one compass direction, i.e East, North, West, or South,
initiates the progression of the spiral.

![7x7 with axes, bearing: south, center: 1000, step: -300](docs/images/spiral_matrix_7+axes+bearing_south+center1000+step-300.png "7x7 with axes, bearing: south, center: 1000, step: -300")

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

#### Options for integer-populated matrix cells

By default, the series of elements that fill the matrix's cells consists of a
sequence of incrementing integers. The value of the initial integer that fills
the center cell defaults to 1, as does the increment value. Either value may be
modified via command-line argument in order to change the contents of the
resulting matrix. Any positive or negative integer, or zero, is allowable to
occupy the center-cell. The increment must be a non-zero integer.

Use of the following options will modify the implementation of the default
behavior.

    --center INTEGER
        This integer value is used to populate the center
        cell. (default: 1)

    --step INTEGER
        This integer value is used to increment the next
        cell's value as the spiral progresses from cell to
        cell. (default: 1)

#### Options for text element-populated matrix cells

As an alternative to the population of the cells of the matrix with a
progression of incrementing integers, a string of space-delimited text
elements can be supplied. This string of elements might consist of any
combination of words, numbers, punctuation, or whitespace. The text elements
will be read from a file or stdin, or provided via the command-line.

![5x5 with axes, bearing: south, series: lorem_ipsum](docs/images/spiral_matrix_5+axes+bearing_south+right+file_lorem_ipsum.png "5x5 with axes, bearing: south, series: lorem_ipsum")

Use of either of the following options will replace the default behavior of
using incrementing integers to populate the cells.

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

![9x9, spiral: right, series: stormy_night](docs/images/spiral_matrix_9+right+words_stormy_night.png "9x9, spiral: right, series: stormy_night")

###### License: GPL3+
###### Document version: 1.0
###### Modified: 01/11/2018
###### Author: David Schenck
