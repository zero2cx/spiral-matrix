# The SpirtalMatrix API Interface

The SpiralMatrix class instantiates an object which generates a spiral-matrix of
cells according to the caller's specification parameters. The module is written
in Python 3.x and is imported into your project with `import SpiralMatrix`.

For details of the command-line interface for this module, please [click here](../README.md "The command-line interface").

Once instantiated, the constructed matrix object is resident in memory. The
printing to the console of that object's `.matrix` attribute can be accomplished
manually or via the object's `.show()` method.


---
### class SpiralMatrix(dimension [, axes] [, right] [, bearing] [, start] [, step] [, file] [, words])


#### Usage:
    >>> myMatrix = SpiralMatrix(9)
    >>> print(myMatrix.dimension)
    9
    >>> print(myMatrix.max)
    81
    >>> print(myMatrix.matrix)
    65 64 63 62 61 60 59 58 57
    66 37 36 35 34 33 32 31 56
    67 38 17 16 15 14 13 30 55
    68 39 18  5  4  3 12 29 54
    69 40 19  6  1  2 11 28 53
    70 41 20  7  8  9 10 27 52
    71 42 21 22 23 24 25 26 51
    72 43 44 45 46 47 48 49 50
    73 74 75 76 77 78 79 80 81

#### Instance attributes:


###### Always utilized:
- **dimension** - the count of rows and columns in the matrix _(Required parameter)_
- **axes** - enable or disable the printing of axes-labels _(default: False)_
- **turn** - the direction of the spiral, i.e. winding to the left, or to the right _(default: 'left')_
- **bearing** - the compass direction that initiates the spiral progression _(default: 'EAST')_
- **max** - the length of the series of values used to fill the cells
- **origin** - the cell coordinates of the center cell
- **series** - the series of values that will populate the cells of the matrix
- **width** - the width (in characters) of the widest element of series


###### Utilized only in the first instance style  (the default style):
- **start** - the integer value that fills the center cell, i.e. the start of the spiral
- **step** - the integer value of the incrementing progression


###### Utilized only in the second instance style:
- **file** - the name of the text file containing whitespace-delimited word tokens
- **words** - the string of whitespace-delimited tokens, i.e. words

---
### method show([axes])

#### Usage:
    >>> myMatrix.show(True)
        0  1  2  3  4  5  6  7  8
    0  65 64 63 62 61 60 59 58 57
    1  66 37 36 35 34 33 32 31 56
    2  67 38 17 16 15 14 13 30 55
    3  68 39 18  5  4  3 12 29 54
    4  69 40 19  6  1  2 11 28 53
    5  70 41 20  7  8  9 10 27 52
    6  71 42 21 22 23 24 25 26 51
    7  72 43 44 45 46 47 48 49 50
    8  73 74 75 76 77 78 79 80 81

#### Method parameter:
- **axes** - enable or disable the printing of axes-labels

---

###### License: GPL3+
###### Document version: 1.0
###### Modified: 01/13/2018
###### Author: David Schenck
