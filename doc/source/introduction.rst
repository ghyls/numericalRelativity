.. _introduction:


This documentation was written by Mario González and Diego Valledor in 2019.
The files referred in this document are stored in our Github repository_. 

.. _repository: https://github.com/mariohyls/numericalRelativity



====================
Numerical Relativity
====================


On this guide, we will cover the basic usage of every tool we have created.
They essentially consist in various scripts in C++, Fortran and Python, most of
them merged under an interfaced application built with PyQt5. 

Those files, and their basic usage are:

    **riem.py**: calculates symbollicaly any component of the Riemann tensor from
    any metric up to 4 dimensions

    **christ.py** calculates symbollicaly any Cristoffel symbol, also from a
    metric up to 4D.

    **app.py** written using PyQt5 libraries, builds an interface for the two
    previous applications.

    **newtonMulti.py**: Computes, for a given number of cosmological objects, a
    2D simulation uisng a newtonian potential (non relativistic). It considers
    the changes in the mass and in the angular momentum in each collision, and
    builds the trayectory for all the particles using the potential created for
    the rest. Prints the result in a file called by default "data.txt"

    **einsteinMulti.cpp**: Does the same as *newtonMulti*, but an option is
    added to perform the calculations with Swartchild potential, instead of
    newton's one. It is also much more optimized in terms of performance.

    **mercury.py**: plots the trayectory of mercury around the Sun, using both a
    newtonian potential and a version with a small relativistic correction. It
    uses only standard python libraries like *matplotlib*. 

    **simulFromData.py**: It reads the data written by newtonMulti.py or
    einsteinMulti.cpp and plots it in an efficient way, by using pyqtgraph.

In the following sections, we will cover the basic usage of these files, also
providing some examples and discussing some computaitonal issues.






