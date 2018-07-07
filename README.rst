######################################################################################
Genetic algorithms applied in Computer Fluid Dynamics for multiobjective optimization
######################################################################################

.. |orcid| image:: https://img.shields.io/badge/id-0000--0003--2636--3128-a6ce39.svg
   :target: https://orcid.org/0000-0003-2636-3128
   :align: middle

.. |Rfmuxmuy| image:: https://latex.codecogs.com/svg.latex?%5Cdpi%7B100%7D%20%5Cbg_white%20%5Csmall%20R%3Df%28%5Cmu_x%2C%5Cmu_y%29
   :alt: Rfmuxmuy
   :align: middle

.. |divisions| image:: https://latex.codecogs.com/svg.latex?%5Cdpi%7B100%7D%20%5Csmall%20%5Cbegin%7Bmatrix%7D%20fCy1%3DcCy3%5Ccdot%20%5Cdfrac%7BcH%7D%7Bf%7D%20%5Clongrightarrow%20fCy2%3D1-fCy1%20%5C%5C%20%5C%5C%20fCx2%3DcCx1%5Ccdot%5Cdfrac%7BcL%7D%7BbC%7D%20%5Clongrightarrow%20fCx1%3D1-fCx2%20%5C%5C%20%5C%5C%20fCx3%3DcCx3%5Ccdot%5Cdfrac%7BcL%7D%7BaC%7D%20%5Clongrightarrow%20fCx4%3D1-fCx3%20%5Cend%7Bmatrix%7D
	:alt: divisions
	:align: center

.. |NCH| image:: https://latex.codecogs.com/svg.latex?%5Cdpi%7B100%7D%20%5Csmall%20%5Cleft.%5Cbegin%7Bmatrix%7D%20%5Ctext%7Bhorizontal%3A%20%7D%5Cdfrac%7BcCx2%5Ccdot%20cL%7D%7BcNx2%5Ccdot%20N%7D%20%5C%5C%20%5C%5C%20%5Ctext%7Bvertical%3A%20%7D%5Cdfrac%7BcCy2%5Ccdot%20cH%7D%7BcNy2%5Ccdot%20NCH%7D%20%5Cend%7Bmatrix%7D%5Cright%5C%7D%20%5Crightarrow%20NCH%3D%20%5Cdfrac%7BcNx2%20%5Ccdot%20cCy2%5Ccdot%20cH%7D%7BcNy2%5Ccdot%20cCx2%5Ccdot%20cL%7D%5Ccdot%20N
	:alt: cellsCavityHeight
	:align: center

.. |NF| image:: https://latex.codecogs.com/svg.latex?%5Cdpi%7B100%7D%20%5Csmall%20%5Cbegin%7Bmatrix%7D%20%5Cleft.%5Cbegin%7Bmatrix%7D%20%5Ctext%7Bhorizontal%3A%20%7D%5Cdfrac%7BcCx2%5Ccdot%20cL%7D%7BcNx2%5Ccdot%20N%7D%20%5C%5C%20%5C%5C%20%5Ctext%7Bvertical%3A%20%7D%5Cdfrac%7BfCy2%5Ccdot%20f%7D%7BfNy2%5Ccdot%20NF%7D%20%5Cxrightarrow%5BfNy1%20%3D%20cNy3%5Ccdot%20%5Cfrac%7BNCH%7D%7BNF%7D%5D%7BfNy2%5Ccdot%20NF%20%3D%20%281-fNy1%29%5Ccdot%20NF%7D%20%5Cdfrac%7Bfy2%5Ccdot%20f%7D%7BNF-%20cNy3%20%5Ccdot%20NCH%7D%20%5Cend%7Bmatrix%7D%5Cright%5C%7D%20%5Crightarrow%20%5C%5C%20%5C%5C%20%5Crightarrow%20NF%3D%20%5Cdfrac%7BfCy2%20%5Ccdot%20f%20%5Ccdot%20cNx2%7D%7BcCx2%5Ccdot%20cL%7D%5Ccdot%20N%20&plus;%20cNy3%5Ccdot%20NCH%20%5Cend%7Bmatrix%7D
	:alt: cellsFreestream
	:align: center

.. |NBC| image:: https://latex.codecogs.com/svg.latex?%5Cdpi%7B100%7D%20%5Csmall%20%5Cbegin%7Bmatrix%7D%20%5Cleft.%5Cbegin%7Bmatrix%7D%20%5Ctext%7Bhorizontal%3A%20%7D%5Cdfrac%7BfCx1%5Ccdot%20bC%7D%7BfNx1%5Ccdot%20NBC%7D%20%5Cxrightarrow%5BfNx2%3DcNx2%5Ccdot%20%5Cfrac%7BN%7D%7BNBC%7D%5D%7BfNx1%5Ccdot%20NBC%3D%281-fNx2%29%5Ccdot%20NBC%7D%20%5Cdfrac%7BfCx1%5Ccdot%20bC%7D%7BNBC-cNx2%5Ccdot%20N%7D%20%5C%5C%20%5C%5C%20%5Ctext%7Bvertical%3A%20%7D%5Cdfrac%7BfCy2%5Ccdot%20f%7D%7BfNy2%5Ccdot%20NF%7D%20%5Cxrightarrow%5B%5D%7B%5Ctext%7Bby%20definition%7D%7D%20%5Cdfrac%7BcCx2%5Ccdot%20cL%7D%7BcNx2%5Ccdot%20N%7D%20%5Cend%7Bmatrix%7D%5Cright%5C%7D%20%5Crightarrow%20%5C%5C%20%5C%5C%20%5Crightarrow%20NBC%3D%20%5Cdfrac%7BfCx1%20%5Ccdot%20bC%20%5Ccdot%20cNx2%7D%7BcCx2%5Ccdot%20cL%7D%5Ccdot%20N%20&plus;%20cNx2%5Ccdot%20N%20%5Cend%7Bmatrix%7D
	:alt: cellsBeforeCavity
	:align: center

.. |NAC| image:: https://latex.codecogs.com/svg.latex?%5Cdpi%7B100%7D%20%5Csmall%20%5Cbegin%7Bmatrix%7D%20%5Cleft.%5Cbegin%7Bmatrix%7D%20%5Ctext%7Bhorizontal%3A%20%7D%5Cdfrac%7BfCx4%5Ccdot%20aC%7D%7BfNx4%5Ccdot%20NAC%7D%20%5Cxrightarrow%5BfNx3%3DcNx3%5Ccdot%20%5Cfrac%7BN%7D%7BNAC%7D%5D%7BfNx4%5Ccdot%20NAC%3D%281-fNx3%29%5Ccdot%20NAC%7D%20%5Cdfrac%7BfCx4%5Ccdot%20aC%7D%7BNAC-cNx3%5Ccdot%20N%7D%20%5C%5C%20%5C%5C%20%5Ctext%7Bvertical%3A%20%7D%5Cdfrac%7BfCy2%5Ccdot%20f%7D%7BfNy2%5Ccdot%20NF%7D%20%5Cxrightarrow%5B%5D%7B%5Ctext%7Bby%20definition%7D%7D%20%5Cdfrac%7BcCx2%5Ccdot%20cL%7D%7BcNx2%5Ccdot%20N%7D%20%5Cend%7Bmatrix%7D%5Cright%5C%7D%20%5Crightarrow%20%5C%5C%20%5C%5C%20%5Crightarrow%20NAC%3D%20%5Cdfrac%7BfCx4%20%5Ccdot%20aC%20%5Ccdot%20cNx2%7D%7BcCx2%5Ccdot%20cL%7D%5Ccdot%20N%20&plus;%20cNx3%5Ccdot%20N%20%5Cend%7Bmatrix%7D
	:alt: cellsAfterCavity
	:align: center

.. |cellsDivision| image:: https://latex.codecogs.com/svg.latex?%5Cdpi%7B100%7D%20%5Csmall%20%5Cbegin%7Bmatrix%7D%20fNx2%3DcNx1%5Ccdot%5Cdfrac%7BN%7D%7BNBC%7D%20%5Clongrightarrow%20fNx1%3D1-fNx2%20%5C%5C%20%5C%5C%20fNx3%3DcNx3%5Ccdot%5Cdfrac%7BN%7D%7BNAC%7D%20%5Clongrightarrow%20fNx4%3D1-fNx3%20%5C%5C%20%5C%5C%20fNy1%3DcNy3%5Ccdot%20%5Cdfrac%7BNCH%7D%7BNF%7D%20%5Clongrightarrow%20fNy2%3D1-fNy1%20%5C%5C%20%5Cend%7Bmatrix%7D
	:alt: cellsDivision
	:align: center

.. |gradings| image:: https://latex.codecogs.com/svg.latex?%5Cdpi%7B100%7D%20%5Cbg_white%20%5Csmall%20g_%7B11%7D%3Dg_%7B13%7D%3D%5Cdfrac%7B1%7D%7Bg_%7B12%7D%7D%20%5Cqquad%20%5Cqquad%20g_%7B14%7D%3Dg_%7B12%7D%20%5Cqquad%20%5Cqquad%20g_%7B22%7D%20%3D%20%5Cdfrac%7B1%7D%7Bg_%7B21%7D%7D%20%5Cqquad%20%5Cqquad%20g_%7B23%7D%3Dg_%7B21%7D
	:alt: gradings
	:align: center

This is a Senior Thesis developed for the BSc Aerospace Engineering at the University of Leon. However, this project was done at the University of Vermont during an exchange program. The main purpose of this thesis was to couple a metaheuristic optimization method, such as genetic algorithm (GA), with aerospace cases simulated with computer fluid dynamics (CFD) that have multiple objectives (MO).

:Author: Javier Lobato Perez |orcid|
:Advisors: Yves Dubief and Rafael Santamaria 
:Institution: University of Vermont - Mechanical Engineering department

The project required some software to be present on the computer in order to properly run it. The requisites are ``python`` (version used was ``3.6.1``) (with either ``jupyter notebook`` or ``jupyter lab`` to execute the notebooks and understand the basics of the process), ``OpenFOAM`` (version 5.00 was used) and ``paraView`` (version 5.4.0). Required Python packages are the basic ``numpy``, ``matplotlib``, ``scipy``, ``numba``, ``sympy``... However ``optunity``, ``prettytable``, ``tdqm`` and ``prettytable`` are required to run every notebook.  The operating system used for Python bash commands and scripting was ``Ubuntu 16.04 LTS``. Compatibility with other OS has not been tested. 

This readme file is structured in two parts. The first one is a quick overview of the project, showing how to further use the code, the analyzed cases, the development of the code and a brief description of all the terms. However, in the second part there is a *folder by folder* analysis that lists the scripts and code of each folder with a brief description to find something in the future with a quick search. 

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

.. raw:: html

	<img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_cylinder/cylinderMeshBC.png" width="500px" alt="cylinderMeshBC">

Mesh was constructed with ``blockMesh`` and faces correspond the different `boundary conditions <https://github.com/jlobatop/GA-CFD-MO/tree/master/cases/NSGA_cylinder/baseCase>`_ having that the grey face is the flowControl patch where the blowing & suction mechanism is located. The optimization problem has as search variables the amplitude and frequency of a sinusoidal wave that governs the flow control mechanism, that will (certainly) modify the flow field. The standard deviation of the force in the cylinder surface was decomposed in two axis (X and Y) and the objective is to minimize both at the same time. Standard deviation represents not the frequency of the oscillations but its amplitude (trying to reduce it as much as possible).

The individuals in this case don't make a Pareto front but they collapse in two solutions (or cluster of possible solutions). The next figure show these results:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_cylinder/cylOpt.png
	:alt: cylinder_optimization
	:align: center

Some animations of the 'steady-state' of the oscillations ('steady-state' refers here to the time where oscillations where continuous and repetitive) may clarify the behavior of this cylinder:

- Cylinder with the flow control mechanism off:

.. raw:: html

	<img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_cylinder/off.gif" width="600px" alt="flowControlOff">

- Cylinder with the flow control on but a high fitness value (not efficient vortex cancellation):

.. raw:: html

	<img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_cylinder/lowFit.gif" width="600px" alt="lowFitnessIndividual">

- Flow control of the first possible solution:

.. raw:: html

	<img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_cylinder/sol1.gif" width="600px" alt="solution1">

- Flow control of the second possible solution:

.. raw:: html

	<img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_cylinder/sol2.gif" width="600px" alt="solution2">

Convergence in two points may not be the the optimal solution, so further study of this case is required.

Diffuser inlet geometry design
===============================

The inlet of a jet engine determines the state of all the other elements of the enine, having that the overall efficiency will decrease if the diffuser performance it is not on the most optimum value. To increase the efficiency of a diffuser, the pressure ratio between freestream and diffuser outlet must be as high as possible (having a low entropy generation due to supersonic shock waves). The performance of a combustion chamber may also be improved if the Mach number at its inlet is maximum. Thus the parameter space variables are Mach at the diffuser outlet (supossing no turbomachinnery between diffuser and combustion chamber) and the pressure ratio (both will try to be the maximum). The search space variables are the length (L) and angle (theta) of the inlet of the diffuser as depicted by the next figure:

.. raw:: html

	<img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_diffuser/diffuserMesh.png" width="700px" alt="diffuserMesh">

In this case, the results form a Pareto front that separate unfeasible solutions from feasible non-optimal solutions:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_diffuser/diffuserOpt.png
	:alt: diffsuerOptimization
	:align: center

A sample from the first generation may look like:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_diffuser/diffuserGen0.png
	:alt: diffuserFirstGeneration
	:align: center

However, a sample from the last simulated generation looks like:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_diffuser/diffuserLastGen.png
	:alt: diffuserLastGeneration
	:align: center

As it can be seen, the expected case where the shock wave meets the cowl is achieved, along other cases that exchange some pressure ratio for a higher Mach number on the outlet. 

Airfoil shape optimization
===========================

Airfoils are the classical problem of optimization applied to CFD. However, it is usually solved with adjoint methods. In this project, a new approach has been used: geometrical optimization with genetic algorithms. Two parameter space variable cases have been tested, but both depend on the same search space variables. Airfoils have been parametrized with a `Joukowsky transform <https://en.wikipedia.org/wiki/Joukowsky_transform>`_ that depends on mu_x and mu_y as the coordinates of the circle in the Zeta plane. Although it may seem that a circle is fully defined with three parameters (x and y positions of the center and radius), the radius in this case must be `fixed <https://github.com/jlobatop/GA-CFD-MO/blob/master/airfoil-parametrization/joukowsky/Joukowsky_fixedR.ipynb>`_ so the circle always intersects (-1,0) or (1,0), having two possible circles in the Zeta plane (and keeping the one that faces the freestream from left to right). Making the restriction that |Rfmuxmuy| instead of having a `variable radius <https://github.com/jlobatop/GA-CFD-MO/blob/master/airfoil-parametrization/joukowsky/Joukowsky_variableR.ipynb>`_, the shape obtained in the zeta plane will look like as an airfoil (more or less) and weird self-intersecting shapes will be avoided. 

Before showing up the results of the two different optimization, it is worth noticing that the only differences between the two is just one Python script used to include a different fitness computation (and its reference in the `fitness.py`). This shows the adaptability of the code. 

The mesh has been previously designed in 6 blocks that have a diamond-shaped airfoil in the center that is converted to an airfoil depending on the values of mu_x and mu_y of the Joukowsky transform by applying ``blockMesh`` to a file with the coordinates of the transformation:

.. raw:: html

	<table>
	    <tr>
	        <td><img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowskyCDCL/joukRombo.png" width="440px" alt="joukowskyRhombus"></td>
	        <td><img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowskyCDCL/joukFoil.png" width="440px" alt="joukowskyAirfoil"></td>
	    </tr>
	</table>	

Lift and drag 
--------------

The first case, the two parameter space variables that have been tried are the classical lift versus drag comparison. There is a trade-off between lift and drag in airfoils, as it can be seen in the majority of the polar diagrams. The results after the optimization process is:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowskyCDCL/cLcDopt.png
	:alt: liftDrag_Optimization
	:align: center

One sample of the first generation is:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowskyCDCL/joukClCdgen0.png
	:alt: liftDrag_firstGeneration
	:align: center

Three airfoils taken from the last generation show that the airfoils are thin and have a wide variety of curvatures:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowskyCDCL/joukClCdLastGen.png
	:alt: liftDrag_lastGeneration
	:align: center

Lift-to-drag ratio and area 
----------------------------

The search space x and y axis are the same as before, bur the distribution of the Pareto front is different. The parameter space has different variables: Lift-to-drag ratio and area. Both are tried to be maximized:


.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowsky/LDAopt.png
	:alt: liftdragArea_Optimization
	:align: center

A sample of the first generation is the one shown in the image below (but the sample for the initial generation shown in the `previous section <https://github.com/jlobatop/GA-CFD-MO#lift-and-drag>`_ would be also a valid sample because Sobol initialization was used, which is a quasi-random low discrepancy sequences that returns the same sampling points for both cases):

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowsky/joukLDAgen0.png
	:alt: liftdragArea_firstGeneration
	:align: center

However the results in this case are way different from the ones before. These have a larger inner area of the airfoil for most of the cases or a higher curvature:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cases/NSGA_joukowsky/joukLDAlastGen.png
	:alt: liftdragArea_lastGeneration
	:align: center

Conclusions
============

The main objective of the project of coupling genetic algorithms with computer fluid dynamics cases has been fulfilled. The created scripts have been used for three different cases, proving that GA are a good approach to CFD but (at this thesis moment) only for 2D simple cases, given that each one of the optimization process took ~15 hours and created roughly 50 Gb of data. Further developments should aim towards a higher convergence of the Pareto front to reduce both computational time and used space, so this method can be used for more complex cases or even 3D meshes. 

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

.. raw:: html

	<img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/airfoil-parametrization/joukowsky/variableR.png" width="600px" alt="variableRadius">

whereas the transformation with *fixed radius* give two possible airfoils:

.. raw:: html

	<img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/airfoil-parametrization/joukowsky/fixedR.png" width="600px" alt="fixedRadius">
 
These codes have also been coded to be interactive, having sliders to change the center (and the radius when it is variable). The two ``.py`` files are interactive figures with sliders and to run them just execute ``python *.py`` in the terminal.

NACA4
------

The notebook has coded the required `equations <http://www.aerospaceweb.org/question/airfoils/q0041.shtml>`_ to compute a NACA 4-digit series airfoil, different grading tools to get points over certain range, interpolation of an airfoil over certain points (not very useful with airfoils whose equation is known though), and storage of the points in a `.csv` in a sorted way beginning from the trailing edge towards the leading edge over the upper surface and then back over the lower surface.

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

cavity-mesh
============

Mesh generator of a cavity inside a freestream flow with a high level of customization but keeping in mind one objective: maintain the aspect ratio with a value of 1 in the vast majority of the cells that are far from the boundary layer. Basic inputs are the dimensions of the case, having three horizontal dimensions (freestream *beforeCavity* **bC**, horizontal *cavityLength* **cL**, freestream *afterCavity* **aC**) and two vertical ones (*cavityHeight* **cH** and *freestream* height **f**), number of horizontal cells in the cavity (*N*) and grading (boundary layer expansion ratio factor) of the most-left wall and lower wall of the cavity (*g12* and *g21*).  There are additional inputs to the case that may also be varied: z-direction components (z1 and z2) and percentage of the chord and cells for each percentage in the cavity block (cCx1, cCx2, cCx3, cCy1, cCy2, cCy3, cNx1, cNx2, cNx3, cNy1, cNy2, cNy3). Custom gradings for all the other walls are also additional inputs, but if not specified they will be computed automatically depending on the ones fixed for the other directions. 

The inputs are shown in the next figure, having red for the mandatory inputs, blue for the additional ones and black for the ones that will be computed (unless otherwise specified):

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cavity-mesh/input.png
	:alt: inputValues
	:align: center

The computed values are sketched in the figure below:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cavity-mesh/computed.png
	:alt: outputValues
	:align: center

First of all, the dimensions x1, x2, x3, y1 and y2 are computed with the specified individual dimensions. There are some values in the previous sketch that are straightforward to compute, having that the different divisions of each block are computed by:

|divisions|

Number of cells for each dimension are computed so the greatest part of all blocks are squared cells with aspect ratio 1:1. To make that, the distance in the horizontal and vertical dimension of every cell are equaled and solved to get the number of cells in each direction. Keep in mind that total length times the length percentage divided by the total number of cells and by the percentage of cells will give the size of the cell.

- Cavity cell to obtain cells in the cavity height:

|NCH|

- Freestream right-above-the-cavity cell to determine number of cells in the freestream:

|NF|

- Freestream before-the-cavity cell to obtain cells in the horizontal before-the-cavity length:

|NBC|

- Freestream after-the-cavity cell to obtain cells in the horizontal after-the-cavity length:

|NAC|

All the number of cell computations were rounded to the nearest integer to avoid decimal number of cells. Once the number of cells of each block has been computed, it is important to assign the percentage of cells for each block subdivision:

|cellsDivision|

Finally, the different boundary layer inflations are computed by:

|gradings|

unless otherwise specified.

It can be seen in the next figure how a cavity mesh is obtained from some values It is worth noticing that the freestream and a considerable section of the cavity is made of squared cells:

.. image:: https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cavity-mesh/cavity_mesh.png
	:alt: cavityMesh
	:align: center

This folder is in this repository because cavity vortex shedding was an idea which seemed also interesting to control with genetic algorithms. However, time did not let its implementation.

cylinder-mesh
==============

mesh-convergence
-----------------

mesh-flowControl
-----------------

.. raw:: html

	<table>
	    <tr>
	        <td><img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cylinder-mesh/backFC.png" width="290px" alt="backFC"></td>
	        <td><img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cylinder-mesh/refinedBackFC.png" width="290px" alt="refinedBackFC"></td>
	        <td><img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/cylinder-mesh/upperFC.png" width="290px" alt="upperFC"></td>
		</tr>
	</table>

diffuser-mesh
==============

.. image:: ttps://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/diffuser-mesh/diffuserMesh.png
	:alt: diffuserMeshParaFoam
	:align: center

mesh-generation
================

extMesh
--------

.. raw:: html

	<img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/mesh-generation/2412.png" width="600px" alt="externalFlowMesh">

int
----

.. raw:: html

	<img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/mesh-generation/int2412.png" width="600px" alt="internalFlowMesh">


joukowskyMesh
--------------

.. raw:: html

	<img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/mesh-generation/joukowskyAirfoil.png" width="600px" alt="joukowskyMesh">


str_uns
--------

.. raw:: html

	<table>
	    <tr>
	        <td><img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/mesh-generation/structuredCylinder.png" width="440px" alt="structuredMesh"></td>
	        <td><img src="https://raw.githubusercontent.com/jlobatop/GA-CFD-MO/master/docs/mesh-generation/unstructuredCylinder.png" width="440px" alt="unstructuredMesh"></td>
	    </tr>
	</table>	

openFoam-case
==============

(classical pitzdaily with different velocities and simplified mesh for quicker runs)

The initial folder layout::

    case/
    ├── baseCase/
    │   ├── 0/
    │   ├── constant/
    │   └── system/
    └── run/
        ├── allRun.py
        └── plotting.py

The final folder structure::

   case/
    ├── baseCase/
    │   ├── 0/
    │   ├── constant/
    │   └── system/
    └── run/
        ├── generation0/
	    │   ├── ind0/
	    │   │   ├── sim/
	    │   │   │   ├── 0/
	    │   │   │   ├── ...
	    │   │   │   ├── constant/
	    │   │   │   └── system/
	    │   │   ├── continuity.png
	    │   │   ├── forces.png
	    │   │   └── residuals.png
	    │   ├── ...
	    │   └── ind$N/
        ├── ...
        ├── generation$gL/
        ├── allRun.py
        └── plotting.py


optimization
=============

.. image:: https://media.giphy.com/media/o5oLImoQgGsKY/giphy.gif

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

Analysis of vortex + BC definitions

***********
REFERENCES
***********

.. [1] Sóbester, András, and Alexander IJ Forrester. Aircraft aerodynamic design: geometry and optimization. John Wiley & Sons, 2014.

.. [2] Deb, Kalyanmoy, et al. "A fast and elitist multiobjective genetic algorithm: NSGA-II." IEEE transactions on evolutionary computation 6.2 (2002): 182-197. 

.. [3] Townsend, A. A. R. "Genetic Algorithm-A Tutorial." Av.: `https://pdfs.semanticscholar.org/eccb/f6523d2d29a5f6dbed9d7a0210e5ded49b96.pdf <https://pdfs.semanticscholar.org/eccb/f6523d2d29a5f6dbed9d7a0210e5ded49b96.pdf>`_ (2003).

.. [4] Schaffer, J. David. "Multiple objective optimization with vector evaluated genetic algorithms." Proceedings of the First International Conference on Genetic Algorithms and Their Applications, 1985. Lawrence Erlbaum Associates. Inc., Publishers, 1985.

.. [5] Fonseca, Carlos M., and Peter J. Fleming. "Multiobjective genetic algorithms." Genetic algorithms for control systems engineering, IEE colloquium on. IET, 1993.

.. [6] Yen, Gary G., and Haiming Lu. "Dynamic multiobjective evolutionary algorithm: adaptive cell-based rank and density estimation." IEEE Transactions on Evolutionary Computation 7.3 (2003): 253-274.