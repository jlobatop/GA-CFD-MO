######################################################################################
Genetic algorithms applied in Computer Fluid Dynamics for multiobjective optimization
######################################################################################

.. |triki| image:: https://media.giphy.com/media/o5oLImoQgGsKY/giphy.gif

.. |orcid| image:: https://img.shields.io/badge/id-0000--0003--2636--3128-a6ce39.svg
   :target: https://orcid.org/0000-0003-2636-3128
   :align: middle

.. |mathTest| image:: https://www.codecogs.com/eqnedit.php?latex=x&plus;\partial&space;x
   :target: https://latex.codecogs.com/gif.latex?x&plus;\partial&space;x
   :align: middle

This is a Senior Thesis developed for the BSc Aerospace Engineering at the University of Leon. However, this project was done at the University of Vermont during an exchange program. The main purpose of this thesis was to couple a metaheuristic optimization method, such as genetic algorithm (GA), with aerospace cases simulated with computer fluid dynamics (CFD) that have multiple objectives (MO).

:Author: Javier Lobato Perez |orcid|
:Advisors: Yves Dubief and Rafael Santamaria 
:Institution: University of Vermont - Mechanical Engineering department

The project required some software to be present on the computer in order to properly run it. The requisites are ``python`` (version used was ``3.6.1``) (with either ``jupyter notebook`` or ``jupyter lab`` to execute the notebooks and understand the basics of the process), ``OpenFOAM`` (version 5.00 was used) and ``paraView`` (version 5.4.0). Required Python packages are the basic ``numpy``, ``matplotlib``, ``scipy``, ``numba``, ``sympy``... However ``optunity``, ``prettytable``, ``tdqm`` and ``prettytable`` are required to run every notebook.  The operating system used for Python bash commands and scripting was ``Ubuntu 16.04 LTS``. Compatibility with other OS has not been tested. 

This readme file is structured by ... (TODO)

The full report of the project is located at `https://github.com/jlobatop/senior-thesis-tex <https://github.com/jlobatop/senior-thesis-tex>`_.

----------------------------------------------------------------

.. contents:: **Table of Contents**
   :depth: 3
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

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_cylinder/cylinderMeshBC.png
	:width: 400pt
	:align: center

Mesh was constructed with ``blockMesh`` and faces correspond the different `boundary conditions <https://github.com/jlobatop/GA-CFD-MO/tree/master/cases/NSGA_cylinder/baseCase>`_ having that the grey face is the flowControl patch where the blowing & suction mechanism is located. The optimization problem has as search variables the amplitude and frequency of a sinusoidal wave that governs the flow control mechanism, that will (certainly) modify the flow field. The standard deviation of the force in the cylinder surface was decomposed in two axis (X and Y) and the objective is to minimize both at the same time. Standard deviation represents not the frequency of the oscillations but its amplitude (trying to reduce it as much as possible).

The individuals in this case don't make a Pareto front but they collapse in two solutions (or cluster of possible solutions). The next figure show these results:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_cylinder/cylOpt.png
	:width: 666pt
	:align: center

Some animations of the 'steady-state' of the oscillations ('steady-state' refers here to the time where oscillations where continuous and repetitive) may clarify the behavior of this cylinder:

- Cylinder with the flow control mechanism off:
	.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_cylinder/off.gif
		:width: 500pt
		:align: center

- Cylinder with the flow control on but a high fitness value (not efficient vortex cancellation):
	.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_cylinder/highFit.gif
		:width: 500pt
		:align: center

- Flow control of the first possible solution:
	.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_cylinder/sol1.gif
		:width: 500pt
		:align: center

- Flow control of the second possible solution:
	.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_cylinder/sol2.gif
		:width: 500pt
		:align: center

Convergence in two points may not be the the optimal solution, so further study of this case is required.

Diffuser inlet geometry design
===============================

The inlet of a jet engine determines the state of all the other elements of the enine, having that the overall efficiency will decrease if the diffuser performance it is not on the most optimum value. To increase the efficiency of a diffuser, the pressure ratio between freestream and diffuser outlet must be as high as possible (having a low entropy generation due to supersonic shock waves). The performance of a combustion chamber may also be improved if the Mach number at its inlet is maximum. Thus the parameter space variables are Mach at the diffuser outlet (supossing no turbomachinnery between diffuser and combustion chamber) and the pressure ratio (both will try to be the maximum). The search space variables are the length (L) and angle (theta) of the inlet of the diffuser as depicted by the next figure:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_diffuser/diffuserMesh.png
	:align: center
	:width: 400pt

In this case, the results form a Pareto front that separate unfeasible solutions from feasible non-optimal solutions:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_diffuser/diffuserOpt.png
	:width: 666pt
	:align: center

A sample from the first generation may look like:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_diffuser/diffuserGen0.png
	:width: 666pt
	:align: center

However, a sample from the last simulated generation looks like:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_diffuser/diffuserLastGen.png
	:width: 666pt
	:align: center

As it can be seen, the expected case where the shock wave meets the cowl is achieved, along other cases that exchange some pressure ratio for a higher Mach number on the outlet. 

Airfoil shape optimization
===========================

Airfoils are the classical problem of optimization applied to CFD. However, it is usually solved with adjoint methods. In this project, a new approach has been used: geometrical optimization with genetic algorithms. Two parameter space variable cases have been tested, but both depend on the same search space variables. Airfoils have been parametrized with a `Joukowsky transform <https://en.wikipedia.org/wiki/Joukowsky_transform>`_ that depends on mu_x and mu_y as the coordinates of the circle in the Zeta plane. Although it may seem that a circle is fully defined with three parameters (x and y positions of the center and radius), the radius in this case must be `fixed <https://github.com/jlobatop/GA-CFD-MO/blob/master/airfoil-parametrization/joukowsky/Joukowsky_fixedR.ipynb>`_ so the circle always intersects (-1,0) or (1,0), having two possible circles in the Zeta plane (and keeping the one that faces the freestream from left to right). Making the restriction that |mathTest| ``R=f(mu_x, mu_y)`` instead of having a `variable radius <https://github.com/jlobatop/GA-CFD-MO/blob/master/airfoil-parametrization/joukowsky/Joukowsky_variableR.ipynb>`_, the shape obtained in the zeta plane will look like as an airfoil (more or less) and weird self-intersecting shapes will be avoided. 

Before showing up the results of the two different optimization, it is worth noticing that the only differences between the two is just one Python script used to include a different fitness computation (and its reference in the `fitness.py`). This shows the adaptability of the code. The mesh has been previously designed in 6 blocks that have a diamond-shaped airfoil in the center as it can be seen in the next figure:


.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowskyCDCL/joukRombo.png
	:width: 400pt
	:align: center

This mesh is converted to an airfoil depending on the values of mu_x and mu_y of the Joukowsky transform by applying ``blockMesh`` to a file with the coordinates of the transformation. One of the possible airfoils is:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowskyCDCL/joukFoil.png
	:width: 400pt
	:align: center

Lift and drag 
--------------

The first case, the two parameter space variables that have been tried are the classical lift versus drag comparison. There is a trade-off between lift and drag in airfoils, as it can be seen in the majority of the polar diagrams. The results after the optimization process is:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowskyCDCL/cLcDopt.png
	:width: 666pt
	:align: center

One sample of the first generation is:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowskyCDCL/joukClCdgen0.png
	:width: 666pt
	:align: center

Three airfoils taken from the last generation show that the airfoils are thin and have a wide variety of curvatures:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowskyCDCL/joukClCdLastGen.png
	:width: 666pt
	:align: center

Lift-to-drag ratio and area 
----------------------------

The search space x and y axis are the same as before, bur the distribution of the Pareto front is different. The parameter space has different variables: Lift-to-drag ratio and area. Both are tried to be maximized:


.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowsky/LDAopt.png
	:width: 666pt
	:align: center

A sample of the first generation is the one shown in the image below (but the sample for the initial generation shown in the `previous section <https://github.com/jlobatop/GA-CFD-MO#lift-and-drag>`_ would be also a valid sample because Sobol initialization was used, which is a quasi-random low discrepancy sequences that returns the same sampling points for both cases):

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowsky/joukLDAgen0.png
	:width: 666pt
	:align: center

However the results in this case are way different from the ones before. These have a larger inner area of the airfoil for most of the cases or a higher curvature:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowsky/joukLDAlastGen.png
	:width: 666pt
	:align: center

Conclusions
============

The main objective of the project of coupling genetic algorithms with computer fluid dynamics cases has been fulfilled. The created scripts have been used for three different cases, proving that GA are a good approach to CFD but only for 2D simple cases, given that each one of the optimization process took ~15 hours and created roughly 50 Gb of data. Further developments should aim towards a higher convergence of the Pareto front to reduce both computational time and space, so this method can be used for more complex cases or even 3D meshes. 

*****************
FOLDER BY FOLDER
*****************

A more detailed view of the project will be presented here, explaining folder by folder the notebooks and Python scripts that are in the repository.

----------------------------------------------------------------

12-steps-CFD
=============

This folder contains the 12 notebooks of the `MOOC course <http://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/>`_ that  Professor Lorena Barba kindly created with some of her post-doc students and it is a great introduction to CFD via Python notebooks and easily understandable equations. So before using any bigger computer fluid dyanmics suite (as OpenFOAM) a basic knowleddge on how does it works is required to take the most out of it (and without making large mistakes). 

----------------------------------------------------------------

airfoil-parametrization
========================

Three different airfoil parametrization processes have been carried out, having one folder for each one.

airfoil
--------

Notebook to read airfoil points from a data file (as the ones that can be downloaded from `airfoiltools <http://airfoiltools.com/>`_), sort and convert them to upper and lower surfaces. Some function are included to give more detail to the available points, i.e., get 150 points from an airfoil with 50 points with spline interpolation (including also a grading in the x-axis to get the higher point density where desired).

joukowsky
----------

The `Joukowsky transform <https://en.wikipedia.org/wiki/Joukowsky_transform>`_ has been coded in a detailed notebook for a circle defined with three parameters (position of the center and `variable radius <https://github.com/jlobatop/GA-CFD-MO/blob/master/airfoil-parametrization/joukowsky/Joukowsky_variableR.ipynb>`_) and a circle defined only with the center (having a `fixed radius <https://github.com/jlobatop/GA-CFD-MO/blob/master/airfoil-parametrization/joukowsky/Joukowsky_fixedR.ipynb>`_ so the circle always goes through points (1,0) and (-1,0), having shapes that look like airfoils). Joukowsky transformation with *variable radius* may create outputs like:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/airfoil-parametrization/joukowsky/variableR.png
	:width: 500pt
	:align: center

whereas the transformation with *fixed radius* give two possible airfoils:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/airfoil-parametrization/joukowsky/fixedR.png
	:width: 500pt
	:align: center

These codes have also been coded to be interactive, having sliders to change the center (and the radius when it is variable). The two ``.py`` files in this folder are the two different cases presented and to run them just execute ``python *.py`` (tested with ``Python 3.6.1``).

NACA4
------

The notebook has coded the `equations <http://www.aerospaceweb.org/question/airfoils/q0041.shtml>`_ to compute a NACA 4-digit series airfoil, different grading tools to get points over certain range, interpolation of an airfoil (not very useful with airfoils which equation is known though) over certain points, and storage of the points in a `.csv` in a sorted way beginning from the trailing edge towards the leading edge over the upper surface and then back over the lower surface.

----------------------------------------------------------------

cases
======

This folder contains the initial folders for the fours cases introduced above (NSGA_cylinder, NSGA_diffuser, NSGA_joukowsky, NSGA_joukowskyCLCD). It also contains the results of these four simulations (these will differ due to the stochasticity of the algorithm) in the folder `results/ <https://github.com/jlobatop/GA-CFD-MO/tree/master/cases/results>`_ .

templateCase
-------------

This folder contains the basic files, although they **must** be customized for the desired case.

``evolution.py``
	Optimization script with the basics of the algorithm 

``fitness.py``
	Script to group the search space and parameter space variables of each generation in a compact file, saving the values of all individuals

``initialization.py``
	Script to create the first initial population. There are three different initializations: random population, quasi-random low discrepancy sampling (Sobol sequences) or an equi-spaciated population. Although the initialization method should not be relevant (a number high enough of generations should yield the same results regardless of the initial generation), choose carefully because CFD simulations take longer than a simple function evaluation (thus Sobol was usually chosen so different parameter space objectives may be used).

``problemSetup.py``
	This file contains the basics of the case such as the search space constraints or the number of individuals per generation

``run``
	Bash script that will encompass the whole optimization process. This script is responsible of calling the different Python scripts, create the folders to store the data and advance in the generation count. 

``runGen``
	Bash script to manage each generation: beginning with the 
	Distribution of the available number of processors (``procLim``) for the individuals of the generation (``nProc``), so all the processors that are desired to be running at the same time will be running. 
	decomposing the case, openMPI, reconstruct par (though not esential for case analysis)
	Manages the process identifies (PID) of the different simulation, so once a simulation has finished, another one begins. 
	Postprocessing and fitness evaluation


The things that are required to be changed before running the optimization to the case are listed below:

- Include the ``baseCase`` folder

- asd

- Code commands in ``runGen`` if required: such as ``blockMesh`` for the pre-processing part of the simulation or some fitness evaluation commands (e.g. ``pvbatch``).

- Change the name of the files according to the variables (only if desired, not required)

- Modify the fitness script

There are four working cases in the repository with all required files to complete the optimization. These may serve also as further reference. 

----------------------------------------------------------------

cavity-mesh
============

Mesh generator of a cavity inside a freestream flow with a high level of customization but keeping in mind one objective: maintain the aspect ratio with a value of 1 in the vast majority of the cells that are apart from the boundary layer. Basic inputs are the dimensions of the case, having three horizontal dimensions (freestream *before the cavity*, *horizontal length of the cavity*, freestream *after the cavity*) and two vertical ones (*cavity height* and *freestream* height), number of horizontal cells in the cavity and grading (boundary layer expansion ratio factor) of the most-left wall and lower wall of the cavity.  There are additional inputs to the case that may also be varied: z-direction components (z1 and z2) and percentage of the chord and cells for the cavity block (cCx1, cCx2, cCx3, cCy1, cCy2, cCy3, cNx1, cNx2, cNx3, cNy1, cNy2, 
cNy3). Custom gradings for all the other walls are also additional inputs, but if not specified they will be computed automatically depending on the ones fixed for the other directions. 

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cavity-mesh/input.png
	:width: 500pt
	:align: center


.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cavity-mesh/computed.png
	:width: 500pt
	:align: center

The computed values of the variables indicated in the above figure are:



----------------------------------------------------------------

cylinder-mesh
==============

mesh-convergence
-----------------

mesh-flowControl
-----------------

----------------------------------------------------------------

diffuser-mesh
==============

|triki|

----------------------------------------------------------------

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

----------------------------------------------------------------

openFoam-case
==============

----------------------------------------------------------------

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

----------------------------------------------------------------

vortex-generation (temporal math LaTeX testing zone)
=====================================================

:math:`A_\text{c} = (\pi/4) d^2`.

|mathTest|

***********
REFERENCES
***********

.. [1] Sóbester, András, and Alexander IJ Forrester. Aircraft aerodynamic design: geometry and optimization. John Wiley & Sons, 2014.

.. [2] Deb, Kalyanmoy, et al. "A fast and elitist multiobjective genetic algorithm: NSGA-II." IEEE transactions on evolutionary computation 6.2 (2002): 182-197. 

.. [3] Townsend, A. A. R. "Genetic Algorithm-A Tutorial." Av.: `https://pdfs.semanticscholar.org/eccb/f6523d2d29a5f6dbed9d7a0210e5ded49b96.pdf <https://pdfs.semanticscholar.org/eccb/f6523d2d29a5f6dbed9d7a0210e5ded49b96.pdf>`_ (2003).

.. [4] Schaffer, J. David. "Multiple objective optimization with vector evaluated genetic algorithms." Proceedings of the First International Conference on Genetic Algorithms and Their Applications, 1985. Lawrence Erlbaum Associates. Inc., Publishers, 1985.

.. [5] Fonseca, Carlos M., and Peter J. Fleming. "Multiobjective genetic algorithms." Genetic algorithms for control systems engineering, IEE colloquium on. IET, 1993.

.. [6] Yen, Gary G., and Haiming Lu. "Dynamic multiobjective evolutionary algorithm: adaptive cell-based rank and density estimation." IEEE Transactions on Evolutionary Computation 7.3 (2003): 253-274.