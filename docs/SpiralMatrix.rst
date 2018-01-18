SpirtalMatrix Progamming Interface
==================================

Instantiating the SpiralMatrix class generates a spiral matrix grid
structure that conforms to the parameters passed from the caller. The module
is written in Python 3.x and is imported into your project with
``import spiral_matrix`` or ``from spiral_matrix import SpiralMatrix``.

For details of the command-line interface for this module, please `click
here <../README.rst>`__.

Once instantiated, the object’s `.matrix <#matrix>`__ attribute contains
the generated structure of the spiral matrix. This matrix is a Python list
containing elements that are also lists. Printing to the console or other
manipulation of it can be accomplished by manually looping through the row
and column list elements. Pretty-printing it can be done using the object's
`.show() <#show-axes->`__ method.

--------------

Interface Contents
------------------

-  `SpiralMatrix class <#spiralmatrix-class>`__

   -  `Attributes <#attributes>`__

      -  `dimension <#dimension>`__ - the count of rows or columns
      -  `origin <#origin>`__ - the coordinates of the center cell
      -  `bearing <#bearing>`__ - the `compass
         bearing <#compass-bearings>`__ that
      -  `turn <#turn>`__ - the direction of the spiral, i.e. winding to
         the left, or to the right initiates the spiral progression
         outward from the center
      -  `max <#max>`__ - the count of cells
      -  `series <#series>`__ - the series of values used to populate
         the cells
      -  `width <#width>`__ - the width (in characters) of the widest
         element of `series <#series>`__
      -  `matrix <#matrix>`__ - the `dimension <#dimension>`__-sized
         square-shaped 2-d matrix

   -  `Additional attributes - Default
      style <#attributes---default-style>`__

      -  `start <#start>`__ - the integer value that fills the center
         cell, i.e. the start value of `series <#series>`__
      -  `step <#step>`__ - the integer value of the incrementing
         progression of `series <#series>`__

   -  `Additional attributes - Alternative
      style <#attributes---alternative-style>`__

      -  `file <#file>`__ - name of the text file containing
         whitespace-delimited tokens. i.e. words, etc.
      -  `words <#words>`__ - string of whitespace-delimited tokens,
         i.e. words. etc.

   -  `Class attributes <#class-attributes>`__

      -  `E <#e>`__ - relative-to-current coordinate adjustment towards
         compass-east
      -  `N <#n>`__ - relative-to-current coordinate adjustment towards
         compass-north
      -  `W <#w>`__ - relative-to-current coordinate adjustment towards
         compass-west
      -  `S <#s>`__ - relative-to-current coordinate adjustment towards
         compass-south
      -  `compass <#compass>`__ - map of each string representation to
         the dictionary key used to look up its corresponding tuple
         value
      -  `vector <#vector>`__ - a nested dictionary structure that maps
         each compass-bearing to its relative-left and -right
         compass-bearing

   -  `Public method <#public-method>`__

      -  `.show() <#show-axes->`__ - print the matrix structure to the
         console

--------------

SpiralMatrix class
------------------

SpiralMatrix( `dimension <#dimension>`__ [, `turn <#turn>`__] [, `bearing <#bearing>`__] [, `start <#start>`__] [, `step <#step>`__] [, `file <#file>`__] [, `words <#words>`__] )
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instantiation and usage example:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    >>> from spiral_matrix import SpiralMatrix
    >>> myMatrix = SpiralMatrix(9)
    >>> myMatrix.dimension
    9
    >>> myMatrix.max
    81
    >>> myMatrix.matrix
    [[65, 64, 63, 62, 61, 60, 59, 58, 57],
     [66, 37, 36, 35, 34, 33, 32, 31, 56],
     [67, 38, 17, 16, 15, 14, 13, 30, 55],
     [68, 39, 18, 5, 4, 3, 12, 29, 54],
     [69, 40, 19, 6, 1, 2, 11, 28, 53],
     [70, 41, 20, 7, 8, 9, 10, 27, 52],
     [71, 42, 21, 22, 23, 24, 25, 26, 51],
     [72, 43, 44, 45, 46, 47, 48, 49, 50],
     [73, 74, 75, 76, 77, 78, 79, 80, 81]]

Attributes:
~~~~~~~~~~~

`dimension <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - the count of rows or columns
-  *type* - integer value
-  *note* - constrained to odd integers only
-  *default* - none **(required parameter)**

--------------

`origin <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - the coordinates of the center cell
-  *type* - 2-tuple, (integer value, integer value)
-  *notes:*

   -  zero-based coordinate system
   -  vertical axis first, i.e. (y,x)
   -  computed by formula:

      -  origin = (`dimension <#dimension>`__ // 2,
         `dimension <#dimension>`__ // 2)

--------------

`bearing <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - the `compass bearing <#compass-bearings>`__ that
   initiates the spiral progression outward from the center
-  *type* - string value (case indifferrent)
-  *note* - constrained to:

   -  ‘E’ or ‘East’
   -  ‘N’ or ‘North’
   -  ‘W’ or ‘West’
   -  ‘S’ or ‘South’

-  *default* - ‘E’

--------------

`turn <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - the direction of the spiral, i.e. winding to the
   left, or to the right
-  *type* - string value
-  *note* - constrained to ‘left’ or ‘right’ only
-  *default* - ‘left’

--------------

`max <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - the count of cells
-  *type* - integer value
-  *note* - computed by formula:

   -  max = `dimension <#dimension>`__ \* `dimension <#dimension>`__

--------------

`series <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - the series of values used to populate the cells
-  *type* - list, of length `max <#max>`__
-  *notes:*

   -  `*default style* <#additional-attributes---default-style>`__ -
      list of incrementing integer values
   -  `*alternative
      style* <#additional-attributes---alternative-style>`__ - list of
      caller-supplied word tokens
   -  the default style is over-ridden by the usage of either of these
      attributes:

      -  `file <#file>`__ - name of the text file containing
         whitespace-delimited tokens, i.e. words, etc.
      -  `words <#words>`__ - string of whitespace-delimited tokens,
         i.e. words, etc.

--------------

`width <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - the width (in characters) of the widest element of
   `series <#series>`__
-  *type* - integer value
-  *note* - computed by formula:

   -  len(\ `series <#series>`__)

--------------

`matrix <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - the `dimension <#dimension>`__-sized square-shaped
   2-d matrix
-  *type* - list of lists
-  *notes:*

   -  zero-based grid coordinate system
   -  vertical axis first and horizontal second, i.e. (y,x)
   -  each cell is populated by one element of `series <#series>`__

--------------

Additional attributes - default style:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`start <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - the integer value that populates the center cell,
   i.e. the start value of `series <#series>`__
-  *type* - integer value
-  *note* - any positive, negative, or zero integer value is acceptable
-  *default* - 1

--------------

`step <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - the integer value of the incrementing progression of
   `series <#series>`__
-  *type* - integer value
-  *note* - only a positive or negative, non-zero integer value is
   acceptable
-  *default* - 1

--------------

Additional attributes - alternative style:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`file <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - name of the text file containing whitespace-delimited
   tokens, i.e. words, etc.
-  *type* - local system filename
-  *note* - human-readable text files only
-  *default* - not used

--------------

`words <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - string of whitespace-delimited tokens, i.e. words,
   etc.
-  *type* - string value
-  *note* - when the string value is omitted, then text from stdin is
   accepted
-  *default* - not used

--------------

Class attributes:
~~~~~~~~~~~~~~~~~

Compass bearings:
^^^^^^^^^^^^^^^^^

-  *note* - relative position (i.e. direction) from a specified cell is
   calculated by summing one of the tuple values detailed below with
   that cell’s (y, x) coordinates

`E <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - relative-to-current coordinate adjustment towards
   compass-east
-  *value* - 2-tuple, (0, 1)
-  *note* - 0 along the vertical axis, and +1 along the horizontal axis

--------------

`N <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - relative-to-current coordinate adjustment towards
   compass-north
-  *value* - 2-tuple, (-1, 0)
-  *note* - -1 along the vertical axis, and 0 along the horizontal axis

--------------

`W <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - relative-to-current coordinate adjustment towards
   compass-west
-  *value* - 2-tuple, (0, -1)
-  *note* - 0 along the vertical axis, and -1 along the horizontal axis

--------------

`S <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - relative-to-current coordinate adjustment towards
   compass-south
-  *value* - 2-tuple, (1, 0)
-  *note* - +1 along the vertical axis, and 0 along the horizontal axis

--------------

`compass <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - map of each string representation to the dictionary
   key used to look up its corresponding tuple value
-  *value* - dictionary:

   -  ‘E’: E
   -  ‘EAST’: E
   -  ‘N’: N
   -  ‘NORTH’: N
   -  ‘W’: W
   -  ‘WEST’: W
   -  ‘S’: S
   -  ‘SOUTH’: S

--------------

`vector <#interface-contents>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - a nested dictionary structure that maps each
   compass-bearing to its relative-left and -right compass-bearing
-  *value* - dictionary:

   -  ‘left’

      -  *value* - dictionary:

         -  E: N
         -  N: W
         -  W: S
         -  S: E

   -  ‘right’

      -  *value* - dictionary:

         -  E: S
         -  S: W
         -  W: N
         -  N: E

--------------

Public method:
~~~~~~~~~~~~~~

`.show <#interface-contents>`__\ ( [axes] )
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *description* - print the matrix structure to the console
-  *parameter:*

   -  **axes**

      -  *description* - enable or disable the printing of axes-labels
      -  *type* - boolean value
      -  *default* - False

Usage example:
~~~~~~~~~~~~~~

::

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

--------------

pypi: https://pypi.python.org/pypi/spiral-matrix

code repo: https://github.com/zero2cx/spiral-matrix

license: GPL3+

document version: 1.0

modified: 01/17/2018

author: David Schenck

