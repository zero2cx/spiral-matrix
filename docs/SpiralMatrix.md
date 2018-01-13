# The SpirtalMatrix API Interface

The SpiralMatrix class can instantiate an object which generates a spiral-matrix
of cells according to the caller's specification. The module is written in
Python 3.x. and can be imported with `import SpiralMatrix`. For details on the
command-line interface, please [click here](../README.md "The command-line interface").

Once instantiated, the constructed matrix is resident in memory. The printing to
the console of that object's `.matrix` attribute is most easily accomplished via
the object's `.show()` method.

