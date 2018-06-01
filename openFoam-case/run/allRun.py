##########################################################################################################
# LIBRARY IMPORTING
##########################################################################################################

from tqdm import tqdm
import time
import os
import numpy as np
import matplotlib.pyplot as plt
import time

##########################################################################################################
# FUNCTION DEFINITION
##########################################################################################################

# Function to print a 'string' above the progress bar while it is still running
def print_tqdm(string):
    tqdm.write(string)

# Copy the folder from ./case to ./run returning to ./run
def caseCopy():
    os.chdir("..")
    os.system("cp -r ./baseCase ./run/case")
    os.chdir("run")
    
# Once the simulation is done, transfer the folders from case to the folder of each individual
def folderTransfer(analysisType,i,j):
    numFolder = []
    nonNumFolder = []
    for cFolder in os.listdir('case'):
        if analysisType == 'transient':
            os.system("mv ./case/%s ./generation%i/ind%i/sim/%s" %(cFolder,i,j,cFolder))
        elif analysisType == 'steady':
            if str.isnumeric(cFolder):
                numFolder.append(int(cFolder))
            else:
                nonNumFolder.append(cFolder)
        else:
            print_tqdm('\033[0;33mError in analysisType\033[0m') 
            break
    if analysisType == 'steady':
        os.system("mv ./case/%i ./generation%i/ind%i/sim/%i" %(min(numFolder),i,j,min(numFolder)))
        os.system("mv ./case/%i ./generation%i/ind%i/sim/%i" %(max(numFolder),i,j,max(numFolder)))
        for cFolder in nonNumFolder:
            os.system("mv ./case/%s ./generation%i/ind%i/sim/%s" %(cFolder,i,j,cFolder))

##########################################################################################################
# PARAMETER DEFINITION
##########################################################################################################

analysisType = 'steady' # 'steady' (state) or 'transient' for folder transfer  
generations = 2 
individuals = 2
values = np.array([[10,20],[30,40]]) # values that will take VARIABLE1 in U

# Initial linebreak to leave some space
print_tqdm('\n')

##########################################################################################################
# MAIN FUNCTION
##########################################################################################################

# loop over the number of iterations
for i in range(generations):    
    # if there is not a folder for the current generation, this will create it
    if os.path.isdir("generation%i" %i) == False:
        os.system("mkdir generation%i" %i)
    # if it exists, remove that generation folder
    else:
    	os.system("rm -rf ./generationn%i/" %i)

    # evaluate the function for each individual of the generation
    for j in tqdm(range(individuals),desc="{Generation %2.i}" %i):

        # print the current individual in the CLI
        print_tqdm('Inidividual %i' %j)
                
        # if there is not a folder for the current individual, this will create it
        if os.path.isdir("generation%i/ind%i" %(i,j)) == False:
            os.system("mkdir generation%i/ind%i" %(i,j))

        # if there is not a folder for the current individual simulation, this will create it
        if os.path.isdir("generation%i/ind%i/sim" %(i,j)) == False:
            os.system("mkdir generation%i/ind%i/sim" %(i,j))
        
        # copy the preconfigured case
        caseCopy()
        
        # change a value in simulations to see change 
        os.system("sed -i 's/VARIABLE1/%i/g' ./case/0/U" %values[i,j])

        # print the current state in the CLI
        print_tqdm('    Simulating inidividual %i' %j)

        # simulation of the case saving both stderr and stdout 
        os.system("simpleFoam -case ./case > 'generation%i/ind%i/g%ii%i.txt' 2> 'generation%i/ind%i/error_g%ii%i.txt'" %(i,j,i,j,i,j,i,j))

        # transfer the results to the generation/individual folder
        print_tqdm('    Moving inidividual %i' %j)
        folderTransfer(analysisType,i,j)
        
        # plot the stdout results into some fancy graphs
        print_tqdm('    Plotting inidividual %i' %j)
        os.system("python ./plotting.py ./generation%i/ind%i/ g%ii%i.txt" %(i,j,i,j))
        
        # if the error file is empty, this will erase the output of the solver, keeping only the plots
        if int(os.popen("du -h 'generation%i/ind%i/error_g%ii%i.txt'" %(i,j,i,j)).read()[0]) == 0: 
            os.system("rm 'generation%i/ind%i/g%ii%i.txt'" %(i,j,i,j))
            os.system("rm 'generation%i/ind%i/error_g%ii%i.txt'" %(i,j,i,j))
        # otherwise print error and don't remove the stdout
        else:
            print_tqdm('\033[0;33mError in simulation. Review logfile\033[0m') 
            
        # remove the case folder and begin again
        os.system("rm -r case")
    
    if i+1 != generations:
        # doing things...
        print_tqdm('Evaluating generation fitness...')
        time.sleep(1)

        # do more things...
        print_tqdm('Creating new generation... \n')
        time.sleep(1)