######################################################################################
Genetic algorithms applied in Computer Fluid Dynamics for multiobjective optimization
######################################################################################

.. |triki| image:: https://media.giphy.com/media/o5oLImoQgGsKY/giphy.gif

.. |orcid| image:: https://img.shields.io/badge/id-0000--0003--2636--3128-a6ce39.svg
   :target: https://orcid.org/0000-0003-2636-3128

.. |cylinderBC| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_cylinder/cylinderMeshBC.png

.. |cylinderOpt| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_cylinder/cylOpt.png

.. |cylinderOff| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_cylinder/highFit.gif

.. |cylinderHighFit| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_cylinder/highFit.gif

.. |cylinderSol1| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_cylinder/sol1.gif

.. |cylinderSol2| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_cylinder/sol2.gif

.. |diffuserMesh| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_diffuser/diffuserMesh.png

.. |diffuserOpt| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_diffuser/diffuserOpt.png

.. |diffuserGen0| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_diffuser/diffuserGen0.png

.. |diffuserLastGen| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_diffuser/diffuserLastGen.png

.. |joukowskyRomb| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_joukowskyCLCD/joukRombo.png

.. |joukowskyFoil| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_joukowskyCLCD/joukFoil.png

.. |joukClCdOpt| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_joukowskyCLCD/cLcDopt.png

.. |joukClCdGen0| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_joukowskyCLCD/joukClCdgen0.png

.. |joukClCdLastGen| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_joukowskyCLCD/joukClCdLastGen.png

.. |joukLDAopt| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_joukowsky/LDAopt.png

.. |joukLDAgen0| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_joukowsky/joukLDAgen0.png

.. |joukLDAlastGen| image:: https://github.com/jlobatop/GA-CFD-MO/tree/master/docs/cases/NSGA_joukowsky/joukLDAlastGen.png

This is a Senior Thesis developed for the BSc Aerospace Engineering at the University of Leon. However, this project was done at the University of Vermont during an exchange program. The main purpose of this thesis was to couple a metaheuristic optimization method, such as genetic algorithm (GA), with aerospace cases simulated with computer fluid dynamics (CFD) that have multiple objectives (MO).

:Author: Javier Lobato Perez |orcid|
:Advisors: Yves Dubief and Rafael Santamaria 
:Institution: University of Vermont - Mechanical Engineering department

The project required some software to be present on the computer in order to properly run it. The requisites are ``python3`` (with either ``jupyter notebook`` or ``jupyter lab`` to execute the notebooks and understand the basics of the process), ``OpenFOAM`` (version 5.00 was used) and ``paraView`` (version 5.4.0). Required Python packages are the basic ``numpy``, ``matplotlib``, ``scipy``, ``numba``, ``sympy``... However ``optunity``, ``prettytable``, ``tdqm`` and ``prettytable`` are required to run every notebook.  The operating system used for Python bash commands and scripting was ``Ubuntu 16.04 LTS``. Compatibility with other OS has not been tested. 

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

This repository has all the files of the project from the very beginning. It all started with a search of interesting topics to dig a little further: from the Lorena Barba's awesome `12 steps to Navier Stokes <http://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/>`_. course in Python to different mesh generation tools and airfoil parametrization [1]_. Finally, the objective was to use a genetic algorithm (specifically the NSGA-II: Non-dominated Sorting Genetic Algorithm II [2]_ ) for multiobjective optimization of different computer fluid dynamic cases. 

The basic of genetic algorithms must be briefly described before explaining the project. A genetic algorithm is a metaheuristic stochastical global optimization method based on populations: an initial generation is randomly generated and evaluated, the fitness (a measure of how 'good' does an individual performs within the population) is computed and the individuals with higher fitness are randomly combined and mutated, obtaining a new generation with new individuals (that are again evaluated, looping until a stop condition is reached). The main idea is that *high fitness parents will give high fitness offspring* [3]_ (the fitness value doesn't always increase, but it will not decrease). GA are a good approach to a CFD optimization because no gradient information is required and the structure of the fitness function is fairly simple. Thus, each individual will be a CFD simulation that depends on some *search space variables* (change in boundary conditions, mesh, ...) and it will return (amongst a lot of data) some *parameter space values* outputs of the CFD simulation. Each individual of the GA is defined with search space variables and the values of the parameter space will be used used as fitness value, trying to maximize or minimize it. Multiobjective is referred to the kind of optimization that tries to maximize not one but more objectives at the same time. Usually those objectives are in trade-off (when one is optimized the other has its least optimum value), so one single solution is unfeasible. The Pareto front is the set of possible solutions that optimize all objectives as much as possible. There are a lot of genetic algorithms designed for multiobjective optimization (VEGA [4]_, MOGA [5]_, NSGA-II [2]_, DMOEA [6]_, ...), but the NSGA-II was chosen specially for being a well-tested method, efficient, with a straightforward implementation and without user-defined parameters (that usually condition the suscess of the optimization process).

At this point, the use of an already exiting code of the NSGA-II was an plausible option: there are libraries as `PyGMO <http://esa.github.io/pygmo/index.html>`_ or `Platypus <https://platypus.readthedocs.io/en/latest/index.html>`_ designed for multiobjective optimization in Python. However, as the fitness of the individuals will be determined from a CFD simulation with OpenFOAM, a automatic implementation using only Python was unfeasible (or at least, more complex than mixinng Python and bash scripting). Thus, the NSGA-II was coded up in Python, first in `jupyter notebooks <https://github.com/jlobatop/GA-CFD-MO/blob/master/optimization/NSGA_II.ipynb>`_ (in order to see the different steps of the process) and then it was separated in Python scripts for the different phases of the project (`initialization <https://github.com/jlobatop/GA-CFD-MO/blob/master/cases/templateCase/initialization.py>`_ of the first generation, `fitness <https://github.com/jlobatop/GA-CFD-MO/blob/master/cases/templateCase/fitness.py>`_ evaluation of a generation, `evolution <https://github.com/jlobatop/GA-CFD-MO/blob/master/cases/templateCase/evolution.py>`_ of the generations (taking the fitness of the previous generation and applying selection, crossover and mutation) and `problemSetup <https://github.com/jlobatop/GA-CFD-MO/blob/master/cases/templateCase/problemSetup.py>`_ which includes the constraints of the problem). Other Python scripts may be required for the CFD post-processing of the case and data analysis, as well as ``pvbatch`` scipts for command line manipulation of the case in paraView. Also there are 

The different scripts will refer to text files that store both the search space and the parameter space values for each generation and individuals. Those text files are the outputs of either a genetic algorithm script (search space values are the output of the ``evolution.py``) or a CFD simulation (e.g., the lift and drag are the ``forces`` output of the OpenFOAM simulation). The basic structure of the folder tree before running the algorithm is::

    case/
    ├── baseCase/
    │   ├── 0/
    │   ├── constant/
    │   └── system/
    ├── run.sh
    ├── runGen.sh
    ├── problemSetup.py
    ├── initialization.py
    ├── fitness.py
    └── evolution.py

As said, other scripts may be included if further analysis of the CFD simulation is required. Folder structure will noticeably get larger after the process, having something close to::

    case/
    ├── gen0/
    │   ├── ind0/
    │   │   ├── 0/
    │   │   ├── 1/
    │   │   ├── ...
    │   │   ├── system/
    │   │   ├── constant/
    │   │   ├── postProcessing/
    │   │   ├── BMg0i0
    │   │   ├── RUNg0i0
    │   │   └── g0i0.OpenFOAM
    │   ├── ind1/
    │   │   └── ...
    │   ├── ...
    │   ├── ind$N/
    │   │   └── ...
    │   ├── popX1_0
    │   ├── popX2_0
    │   └── data/  
    │       ├── FITg0i0.txt
    │       ├── FITg0i1.txt
    │       └── ...
    ├── gen1/
    │   └── ...
	├── ...
    ├── gen$gL/
    │   └── ...
    ├── data/
    │   ├── gen0.txt
    │   ├── gen1.txt
    │   └── ...
    ├── baseCase/
    │   ├── 0/
    │   ├── constant/
    │   └── system/
    ├── run.sh
    ├── runGen.sh
    ├── problemSetup.py
    ├── initialization.py
    ├── fitness.py
    └── evolution.py

Not all folder are displayed, using ``$N`` as the number of individuals per generation and ``$gL`` as generation limit. Also depending on the type of solver, more or less folders will be saved, having only folders ``0/`` and ``lastIteration`` for a steady-state solver and all timestep folders for a transient solver. ``BMg0i0`` is the output of the ``blockMesh`` operation for the individial 0 of the generation 0 (just if it is needed for each individual). ``data/`` folder in each generation may store also data as convergence plots (as both joukowsky cases) or plots over a line from paraView (diffuser case). The data used for the Python scripts is stored in ``case/data/``, having a file for each generation that stores ``x1, x2, f1, f2`` for each indidvidual (having that ``x1`` and ``x2`` are the search space variables and ``f1`` and ``f2`` the parameter space variables or objective functions). 

After this brief description of the algorithm and folder structure (and given that documentation of the code is written inside each script), the analysis of the three studied cases will be introduced. If the already existing cases are run again, the individuals will vary due to the stochasticity of the algorithm, but the Pareto front should be close to the one shown below. 

Vortex supression in a cylinder wake
=====================================

A cylinder (amongst a lot of other objects) facing a stream may undergo vortex shedding under certain conditions. Vortex phenomena is associated with strong vibrations and oscillations that may cause structural damage to the object (specially if the frequency of the cylinder matches the natural frequency of the structure). In order to reduce it, different methods can be applied. In this case a passive blowing & suction flow control mechanism (preferred against a blowing mechanism that will not have a zero net momentum in the flow) is located in the rear part of a cylinder following the next schematics:

|cylinderSchematics|

Mesh was constructed with ``blockMesh`` and faces correspond the different `boundary conditions <https://github.com/jlobatop/GA-CFD-MO/tree/master/cases/NSGA_cylinder/baseCase>`_ having that the grey face is the flowControl patch where the blowing & suction mechanism is located. The optimization problem has as search variables the amplitude and frequency of a sinusoidal wave that governs the flow control mechanism, that will (certainly) modify the flow field. The standard deviation of the force in the cylinder surface was decomposed in two axis (X and Y) and the objective is to minimize both at the same time. Standard deviation represents not the frequency of the oscillations but its amplitude (trying to reduce it as much as possible).

The individuals in this case don't make a Pareto front but they collapse in two solutions (or cluster of possible solutions). The next figure show these results:

|cylinderOpt|

Some animations of the 'steady-state' of the oscillations ('steady-state' refers here to the time where oscillations where continuous and repetitive) may clarify the behavior of this cylinder:

- Cylinder with the flow control mechanism off:
	|cylinderOff|

- Cylinder with the flow control mechanism off:
	|cylinderHighFit|

- Cylinder with the flow control mechanism off:
	|cylinderSol1|

- Cylinder with the flow control mechanism off:
	|cylinderSol2|

Diffuser inlet geometry design
===============================

The inlet of a jet engine determines the state of all the other elements of the enine, having that the overall efficiency will decrease if the diffuser performance it is not on the most optimum value. To increase the efficiency of a diffuser, the pressure ratio between freestream and diffuser outlet must be as high as possible (having a low entropy generation due to supersonic shock waves). The performance of a combustion chamber may also be improved if the Mach number at its inlet is maximum. Thus the parameter space variables are Mach at the diffuser outlet (supossing no turbomachinnery between diffuser and combustion chamber) and the pressure ratio (both will try to be the maximum). The search space variables are the length (L) and angle (theta) of the inlet of the diffuser as depicted by the next figure:

|diffuserMesh|

In this case, the results form a Pareto front that separate unfeasible solutions from feasible non-optimal solutions:

|diffuserOpt|

A sample from the first generation may look like:

|diffuserGen0|

However, a sample from the last simulated generation looks like:

|diffuserLastGen|

As it can be seen, the expected case where the shock wave meets the cowl is achieved, along other cases that exchange some pressure ratio for a higher Mach number on the outlet. 

Airfoil shape optimization
===========================

Airfoils are the classical problem of optimization applied to CFD. However, it is usually solved with adjoint methods. In this project, a new approach has been used: geometrical optimization with genetic algorithms. Two parameter space variable cases have been tested, but both depend on the same search space variables. Airfoils have been parametrized with a `Joukowsky transform <https://en.wikipedia.org/wiki/Joukowsky_transform>`_ that depends on mu_x and mu_y as the coordinates of the circle in the Zeta plane. Although it may seem that a circle is fully defined with three parameters (x and y positions of the center and radius), the radius in this case must be `fixed <https://github.com/jlobatop/GA-CFD-MO/blob/master/airfoil-parametrization/joukowsky/Joukowsky_fixedR.ipynb>`_ so the circle always intersects (-1,0) or (1,0), having two possible circles in the Zeta plane (and keeping the one that faces the freestream from left to right). Making the restriction that ``R=f(mu_x, mu_y)`` instead of having a `variable radius <https://github.com/jlobatop/GA-CFD-MO/blob/master/airfoil-parametrization/joukowsky/Joukowsky_variableR.ipynb>`_, the shape obtained in the zeta plane will look like as an airfoil (more or less) and weird self-intersecting shapes will be avoided. 

Before showing up the results of the two different optimization, it is worth noticing that the only differences between the two is just one Python script used to include a different fitness computation (and its reference in the `fitness.py`). This shows the adaptability of the code. The mesh has been previously designed in 6 blocks that have a diamond-shaped airfoil in the center as it can be seen in the next figure:

|joukowskyRomb|

This mesh is converted to an airfoil depending on the values of mu_x and mu_y of the Joukowsky transform by applying ``blockMesh`` to a file with the coordinates of the transformation. One of the possible airfoils is:

|joukowskyFoil| 

Lift and drag 
--------------

The first case, the two parameter space variables that have been tried are the classical lift versus drag comparison. There is a trade-off between lift and drag in airfoils, as it can be seen in the majority of the polar diagrams. The results after the optimization process is:

|joukClCdOpt|

One sample of the first generation is:

|joukClCdGen0|

Three airfoils taken from the last generation show that the airfoils are thin and have a wide variety of curvatures:

|joukClCdLastGen|

Lift-to-drag ratio and area 
----------------------------

The search space x and y axis are the same as before, bur the distribution of the Pareto front is different. The parameter space has different variables: Lift-to-drag ratio and area. Both are tried to be maximized:

|joukLDAopt|

A sample of the first generation is the one shown in the image below (but the sample for the initial generation shown in the `previous section <https://github.com/jlobatop/GA-CFD-MO#lift-and-drag>`_ would be also a valid sample because Sobol initialization was used, which is a quasi-random low discrepancy sequences that returns the same sampling points for both cases):

|joukLDAgen0|

However the results in this case are way different from the ones before. These have a larger inner area of the airfoil for most of the cases or a higher curvature:

|joukLDAlastGen|

Conclusions
============


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

templateCase
-------------

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

vortex-generation (temporal math LaTeX testing zone)
=====================================================


inline math with roles

.. role:: latex(raw)
   :format: latex

:latex:`\\textsc{NoTex}`

inline math

:math: `\frac{ \sum_{t=0}^{N}f(t,k) }{N}`

block math

.. math:: 

	\\frac{ \sum_{t=0}^{N}f(t,k) }{N}

***********
REFERENCES
***********

.. [1] Sóbester, András, and Alexander IJ Forrester. Aircraft aerodynamic design: geometry and optimization. John Wiley & Sons, 2014.

.. [2] Deb, Kalyanmoy, et al. "A fast and elitist multiobjective genetic algorithm: NSGA-II." IEEE transactions on evolutionary computation 6.2 (2002): 182-197. 

.. [3] Townsend, A. A. R. "Genetic Algorithm-A Tutorial." Av.: `https://pdfs.semanticscholar.org/eccb/f6523d2d29a5f6dbed9d7a0210e5ded49b96.pdf <https://pdfs.semanticscholar.org/eccb/f6523d2d29a5f6dbed9d7a0210e5ded49b96.pdf>`_ (2003).

.. [4] Schaffer, J. David. "Multiple objective optimization with vector evaluated genetic algorithms." Proceedings of the First International Conference on Genetic Algorithms and Their Applications, 1985. Lawrence Erlbaum Associates. Inc., Publishers, 1985.

.. [5] Fonseca, Carlos M., and Peter J. Fleming. "Multiobjective genetic algorithms." Genetic algorithms for control systems engineering, IEE colloquium on. IET, 1993.

.. [6] Yen, Gary G., and Haiming Lu. "Dynamic multiobjective evolutionary algorithm: adaptive cell-based rank and density estimation." IEEE Transactions on Evolutionary Computation 7.3 (2003): 253-274.