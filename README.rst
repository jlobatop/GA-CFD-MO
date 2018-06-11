######################################################################################
Genetic algorithms applied in Computer Fluid Dynamics for multiobjective optimization
######################################################################################

.. |triki| image:: https://media.giphy.com/media/o5oLImoQgGsKY/giphy.gif

.. |orcid| image:: https://img.shields.io/badge/id-0000--0003--2636--3128-a6ce39.svg
   :target: https://orcid.org/0000-0003-2636-3128

This is a Senior Thesis developed for the BSc Aerospace Engineering at the University of Leon. However, this project was done at the University of Vermont during an exchange program. The main purpose of this thesis was to couple a heuristic optimization method, such as genetic algorithm (GA), with aerospace cases simulated with computer fluid dynamics (CFD) that have multiple objectives.

:Author: Javier Lobato Perez |orcid|
:Advisors: Yves Dubief and Rafael Santamaria 
:Institution: University of Vermont - Mechanical Engineering department

The project required some software to be present on the computer in order to properly run it. The requisites are ``python3`` (with either ``jupyter notebook`` or ``jupyter lab`` to execute the notebooks and understand the basics of the process), ``OpenFOAM`` (version 5.00 was used) and ``paraView`` (version 5.4.0). Required Python packages are the basic ``numpy``, ``matplotlib``, ``scipy``, ``numba``, ``sympy``... However ``optunity``, ``prettytable``, ``tdqm`` and ``prettytable`` are required to run every notebook.  The operating system used for Python bash commands and scripting was `Ubuntu 16.04 LTS`. Compatibility with other OS has not been tested. 

This readme file is structured by ... (TODO)

The full report of the project is located at `https://github.com/jlobatop/senior-thesis-tex <https://github.com/jlobatop/senior-thesis-tex>`_.

----------------------------------------------------------------

.. contents:: **Table of Contents**
   :depth: 2
   :backlinks: top

----------------------------------------------------------------

***************
QUICK OVERVIEW
***************

This repository has all the files of the project from the very beginning. It all started with a search of interesting topics to dig a little further: from the Lorena Barba's awesome `12 steps to Navier Stokes <http://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/>`_. course in Python to different mesh generation tools and airfoil parametrization. Finally, the objective was to use a genetic algorithm (specifically the NSGA-II (Non-dominated Sorting Genetic Algorithm II) [1]_ ) for multiobjective optimization of different computer fluid dynamic cases. 

At this point, the use of an already exiting code of the NSGA-II was an plausible option: there are even libraries as `PyGMO <http://esa.github.io/pygmo/index.html>`_ or `Platypus <https://platypus.readthedocs.io/en/latest/index.html>`_ designed for multiobjective optimization in Python. However, as the fitness of the individuals will be determined from a CFD simulation with OpenFOAM, a automatic implementation using only Python was unfeasible (or at least, more complex than mixinng Python and bash scripting). Thus, the NSGA-II was coded up in Python, first in `jupyter notebooks <https://github.com/jlobatop/GA-CFD-MO/blob/master/optimization/NSGA_II.ipynb>`_ (in order to see the different steps of the process) and then it was separated in the different phases, 

*****************
FOLDER BY FOLDER
*****************
|triki|

12-steps-CFD
=============

airfoil-parametrization
========================

airfoil
--------

joukowsky
----------

NACA4
------

cases
======

NSGA_cylinder
--------------

NSGA_diffuser
--------------

NSGA_joukowsky
---------------

NSGA_joukowskyCLCD
-------------------

results
--------

sampleCase
-----------

cavity-mesh
============

cylinder-mesh
==============

mesh-convergence
-----------------

mesh-flowControl
-----------------

diffuser-mesh
==============

mesh-generation
================

extMesh
--------

int
----

joukowskyMesh
--------------

str_uns
--------

openFoam-case
==============

optimization
=============

NSGAIIpics
-----------

Pareto_fronts
--------------

comparisonData
---------------

figures
--------

vortex-generation
==================

***********
REFERENCES
***********
.. [1] Deb, Kalyanmoy, et al. "A fast and elitist multiobjective genetic algorithm: NSGA-II." IEEE transactions on evolutionary computation 6.2 (2002): 182-197.