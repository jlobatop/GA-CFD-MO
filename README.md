# senior-thesis
Senior Thesis in Mechanical Engineering at the University of Vermont. Computer fluid dynamics and optimization contents - along other related stuff that interests me. This will keep track of the content of the folders and what is done inside each code. Mostly Python and OpenFOAM codes - although some MATLAB (...) could appear. Eventually this README.md file will become an ordered summary of all the work related to this topic.
 
## 12-steps-CFD
These are the notebooks from the Lorena A. Barba course "*12 steps to CFD*" in Python. They have different stuff from other pages as well as the main equations written on them.


## airfoil-parametrization
In the way of searching a way of correctly parametrize airfoils, different models have been analyzed so far. One of them is the typical NACA 4-digit equations (more info at <https://en.wikipedia.org/wiki/NACA_airfoil>), obtaining the plot of the selected airfoil and a list of points to further pre-processing. Some meshing with this airfoil is attempted - no major success so far. Another option is the Joukowsky transform (more info at <https://en.wikipedia.org/wiki/Joukowsky_transform>), the same process as in the CHMYukovski program, done in previous courses (<https://github.com/jlobatop/CHMYukovski>). The script for the Joukowsky transform with sliders should be run outside Jupyter to have the ability of being interactive.

## cavity-mesh
A cavity mesh for OpenFOAM, attemp to do some vortex in future simulations.

## cylinder-mesh
A simple blockMesh mesh of a cylinder to make some vortex shedding calculations. Different meshes have been made in order to prove mesh convergence and independence of the grid size. The model followed is: 

* original: represents the original mesh

* 2original: level 2 of refinement referred to the original mesh (and so do for 3original)

* original2: reduces one level of refinement the original mesh grid (and so do for original3)

In this folder there are also the different active flow control (AFC) meshes developed. The ones used so far are:

* backAFC: the introduction of momentum is performed in the rear part of the cylinder

* upperAFC: there is one inlet of flow in the upper part of the cylinder

In the future a dual AFC-patch mesh will be created. It will be symmetric to upperAFC but with one exit in the upper part and another one in the lower part. 


## mesh-generation
A python notebook that joins a lot of previously done functions with the purpose of creating the internal mesh (for the moment) of an airfoil selected with a NACA4 code, including an angle of attack variator. The other notebook develops and external flow mesh from a NACA profile and some other parameters. Also a calculator of boundary layer inflation has been added to increase the utility of the external mesh generator.


## openFoam_cases
Folder to store different OpenFOAM cases useful for the thesis or Python scripts to automate different tasks such as automatic evaluation or post-processing.


## optimization
First approach to complex systems: neural networks and genetic algorithms. Given that the problem will be developed as a 2D surface, some <tt> function_optimization </tt> has been performed. The classical Monte Carlo method and an optimized Monte Carlo method have been coded up to this moment. A genetic algorithm approach has been included in order to compute the solution of a multiobjective optimization problem.


## vortex-generation
Once the basic flow over a cylinder has been simulated, the different values will be processes to avoid the vortex generation (or try to). In order to do that, a ParaView script has been made to export PlotOverLine data from all timesteps in a simulation (processed afterwards to avoid 200 files - i.e. timesteps - for each line and packaging them into two file). Furthermore, the data has been processes with Python, figuring out a way to avoid vortex sheding forming with active flow control. Inside the file there's a method to compute different wave parameters from data, obtaining phase angle, amplitude, frequency and offset. 
