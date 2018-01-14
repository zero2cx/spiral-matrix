
# SpirtalMatrix Progamming Interface

The SpiralMatrix class instantiates an object which generates a spiral matrix of
cells according to the specified parameters from the caller. The module is
written in Python 3.x and is imported into your project with `import
spiral_matrix` or `from spiral_matrix import SpiralMatrix`.

For details of the command-line interface for this module, please [click here](../README.md "The command-line interface").

Once instantiated, the object's [`.matrix`](#matrix) attribute contains the
actual matrix structure. The printing to the console or other manipulation of
the [`.matrix`](#matrix) structure can be accomplished manually by looping
through its rows and columns. Pretty-printing it can be done using the
[`.show()`](#show-axes-) method.

---

## Interface Contents
- [SpiralMatrix class](#spiralmatrix-class)
  - [Attributes](#attributes)
    - [dimension](#dimension) - the count of rows or columns
    - [turn](#turn) - the direction of the spiral, i.e. winding to the left, or
    to the right
    - [bearing](#bearing) - the [compass](#compass) bearing that initiates the
    spiral progression
    - [max](#max) - the count of cells
    - [origin](#origin) - the coordinates of the center cell
    - [series](#series) - the series of values used to populate the cells
    - [width](#width) - the width (in characters) of the widest element of
    [series](#series)
    - [matrix](#matrix) - the [dimension](#dimension)-sized square-shaped 2-d
    matrix
  - [Attributes - Default style](#attributes---default-style)
    - [start](#start) - the integer value that fills the center cell, i.e. the
    start value of [series](#series)
    - [step](#step) - the integer value of the incrementing progression of
    [series](#series)
  - [Attributes - Alternative style](#attributes---alternative-style)
    - [file](#file) - name of the text file containing whitespace-delimited word
    tokens
    - [words](#words) - string of whitespace-delimited tokens, i.e. words
  - [Class attributes](#class-attributes)
    - [E](#e) - an equivalent of compass-east
    - [N](#n) - an equivalent of compass-north
    - [W](#w) - an equivalent of compass-west
    - [S](#s) - an equivalent of compass-south
    - [compass](#compass) - map of each string representation to the dictionary
    key, used to look up the corresponding tuple value
    - [vector](#vector) - a nested dictionary structure that maps each
    compass-based vector to its relative-left and -right compass-bearing
    dictionary key
  - [Public method](#public-method)
    - [.show()](#show-axes-) - print the matrix structure to the console

---

## SpiralMatrix class

### SpiralMatrix( [dimension](#dimension) [, [turn](#turn)] [, [bearing](#bearing)] [, [start](#start)] [, [step](#step)] [, [file](#file)] [, [words](#words)] )

### Instantiation and usage example:
    >>> from spiral_matrix import SpiralMatrix
    >>> myMatrix = SpiralMatrix(9)
    >>> print(myMatrix.dimension)
    9
    >>> print(myMatrix.max)
    81
    >>> print(myMatrix.matrix)
    [[65, 64, 63, 62, 61, 60, 59, 58, 57], [66, 37, 36, 35, 34, 33, 32, 31,
    56], [67, 38, 17, 16, 15, 14, 13, 30, 55], [68, 39, 18, 5, 4, 3, 12, 29
    , 54], [69, 40, 19, 6, 1, 2, 11, 28, 53], [70, 41, 20, 7, 8, 9, 10, 27,
    52], [71, 42, 21, 22, 23, 24, 25, 26, 51], [72, 43, 44, 45, 46, 47, 48,
    49, 50], [73, 74, 75, 76, 77, 78, 79, 80, 81]]

### Attributes:


#### [dimension](#interface-contents "Interface Contents")
  - _description_ - the count of rows or columns
  - _type_ - integer value
  - _note_ - constrained to odd integers only
  - _default_ - none **(required parameter)**

---

#### [turn](#interface-contents "Interface Contents")
  - _description_ - the direction of the spiral, i.e. winding to the left, or to
  the right
  - _type_ - string value
  - _note_ - constrained to 'left' or 'right' only
  - _default_ - 'left'

---

#### [bearing](#interface-contents "Interface Contents")
  - _description_ - the [compass](#compass) bearing that initiates the spiral
  progression
  - _type_ - string value (case indifferrent)
  - _note_ - constrained to:
    - 'E' or 'East'
    - 'N' or 'North'
    - 'W' or 'West'
    - 'S' or 'South'
  - _default_ - 'E'

---

#### [max](#interface-contents "Interface Contents")
  - _description_ - the count of cells
  - _type_ - integer value
  - _note_ - computed by formula:
    - max = [dimension](#dimension) * [dimension](#dimension)

---

#### [origin](#interface-contents "Interface Contents")
  - _description_ - the coordinates of the center cell
  - _type_ - 2-tuple, (integer value, integer value)
  - _notes:_
    - zero-based coordinate system
    - vertical axis first, i.e. (y,x)
    - computed by formula:
      - origin = ([dimension](#dimension) // 2, [dimension](#dimension) // 2)

---

#### [series](#interface-contents "Interface Contents")
  - _description_ - the series of values used to populate the cells
  - _type_ - list, of length [max](#max)
  - _notes:_
    - [_default_](#additional-attributes---default-style) - list of incrementing
    integer values
    - [_alternative_](#additional-attributes---alternative-style) - list of
    supplied word tokens
    - the default style is over-ridden by the usage of either of these
    attributes:
      - [file](#file)
      - [words](#words)

---

#### [width](#interface-contents "Interface Contents")
  - _description_ - the width (in characters) of the widest element of
  [series](#series)
  - _type_ - integer value
  - _note_ - computed by formula:
    - len([series](#series))

---

#### [matrix](#interface-contents "Interface Contents")
  - _description_ - the [dimension](#dimension)-sized square-shaped 2-d matrix
  - _type_ - list of lists
  - _notes:_
    - zero-based coordinate system
    - vertical axis first, i.e. (y,x)
    - each cell is populated by one element of [series](#series)

---

### Additional attributes - default style:


#### [start](#interface-contents "Interface Contents")
  - _description_ - the integer value that fills the center cell, i.e. the start
  value of [series](#series)
  - _type_ - integer value
  - _note_ - any positive, negative, or zero integer value is acceptable
  - _default_ - 1

---

#### [step](#interface-contents "Interface Contents")
  - _description_ - the integer value of the incrementing progression of
  [series](#series)
  - _type_ - integer value
  - _note_ - only a positive or negative, non-zero integer value is acceptable
  - _default_ - 1

---

### Additional attributes - alternative style:

#### [file](#interface-contents "Interface Contents")
  - _description_ - name of the text file containing whitespace-delimited word
  tokens
  - _type_ - local system filename
  - _note_ - human-readable text files only
  - _default_ - not used

---

#### [words](#interface-contents "Interface Contents")
  - _description_ - string of whitespace-delimited tokens, i.e. words
  - _type_ - string value
  - _note_ - when the string value is omitted, then text from stdin is accepted
  - _default_ - not used

---

### Class attributes:

#### Compass bearings:
  - _note_ - relative position (i.e. direction) from a specified cell is
  calculated by summing one of the tuple values detailed below with that cell's
  (y, x) coordinates

#### [E](#interface-contents "Interface Contents")
  - _description_ - an equivalent of compass-east
  - _value_ - 2-tuple, (0, 1)
  - _note_ - 0 along the vertical axis, and +1 along the horizontal axis

---

#### [N](#interface-contents "Interface Contents")
  - _description_ - an equivalent of compass-north
  - _value_ - 2-tuple, (-1, 0)
  - _note_ - -1 along the vertical axis, and 0 along the horizontal axis

---

#### [W](#interface-contents "Interface Contents")
  - _description_ - an equivalent of compass-west
  - _value_ - 2-tuple, (0, -1)
  - _note_ - 0 along the vertical axis, and -1 along the horizontal axis

---

#### [S](#interface-contents "Interface Contents")
  - _description_ - an equivalent of compass-south
  - _value_ - 2-tuple, (1, 0)
  - _note_ - +1 along the vertical axis, and 0 along the horizontal axis

---

#### [compass](#interface-contents "Interface Contents")
  - _description_ - map of each string representation to the dictionary key,
  used to look up the corresponding tuple value
  - _value_ - dictionary:
    - 'E': E
    - 'EAST': E
    - 'N': N
    - 'NORTH': N
    - 'W': W
    - 'WEST': W
    - 'S': S
    - 'SOUTH': S

---

#### [vector](#interface-contents "Interface Contents")
  - _description_ - a nested dictionary structure that maps each compass-based
  vector to its relative-left and -right compass-bearing dictionary key
  - _value_ - dictionary:
    - 'left'
      - _value_ - dictionary:
        - E: N
        - N: W
        - W: S
        - S: E
    - 'right'
      - _value_ - dictionary:
        - E: S
        - S: W
        - W: N
        - N: E

---

### Public method:

#### [.show](#interface-contents "Interface Contents")( [axes] )
  - _description_ - print the matrix structure to the console
  - _parameter:_
    - **axes**
      - _description_ - enable or disable the printing of axes-labels
      - _type_ - boolean value
      - _default_ - False


### Usage example:
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
<!---
    >>> myMatrix.show()
    65 64 63 62 61 60 59 58 57
    66 37 36 35 34 33 32 31 56
    67 38 17 16 15 14 13 30 55
    68 39 18  5  4  3 12 29 54
    69 40 19  6  1  2 11 28 53
    70 41 20  7  8  9 10 27 52
    71 42 21 22 23 24 25 26 51
    72 43 44 45 46 47 48 49 50
    73 74 75 76 77 78 79 80 81 --->

---

###### PyPI: [presently unsubmitted]
###### Repo: [https://github.com/zero2cx/spiral-matrix](https://github.com/zero2cx/spiral-matrix)
###### License: GPL3+
###### Document version: 1.0
###### Modified: 01/13/2018
###### Author: David Schenck
