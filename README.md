# senior-thesis
Senior Thesis in Mechanical Engineering at the University of Vermont. Computer fluid dynamics and optimization contents - along other related stuff that interests me. This will keep track of the content of the folders and what is done inside each code. Mostly Python and OpenFOAM codes - although some MATLAB (...) could appear. Eventually this README.md file will become an ordered summary of all the work related to this topic.
 
## 12-steps-CFD
These are the notebooks from the Lorena A. Barba course "*12 steps to CFD*" in Python. They have different stuff from other pages as well as the main equations written on them.


## airfoil-parametrization
In the way of searching a way of correctly parametrize airfoils, different models have been analyzed so far. One of them is the typical NACA 4-digit equations (more info at <https://en.wikipedia.org/wiki/NACA_airfoil>), obtaining the plot of the selected airfoil and a list of points to further pre-processing. Some meshing with this airfoil is attempted - no major success so far. Another option is the Joukowsky transform (more info at <https://en.wikipedia.org/wiki/Joukowsky_transform>), the same process as in the CHMYukovski program, done in previous courses (<https://github.com/jlobatop/CHMYukovski>). The script for the Joukowsky transform with sliders should be run outside Jupyter to have the ability of being interactive.

## mesh-generation
A python notebook that joins a lot of previously done functions with the purpose of creating the internal mesh (for the moment) of an airfoil selected with a NACA4 code, including an angle of attack variator. The other notebook develops and external flow mesh from a NACA profile and some other parameters. Also a calculator of boundary layer inflation has been added to increase the utility of the external mesh generator.

## optimization
First approach to complex systems: neural networks and genetic algorithms - with hopes to use them in the future optimization of the project.

## cylinder-mesh
A simple blockMesh mesh of a cylinder to make some vortex shedding calculations.

## cavity-mesh
A cavity mesh for OpenFOAM, attemp to do some vortex in future simulations.