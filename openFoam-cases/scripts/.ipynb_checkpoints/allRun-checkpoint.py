##########################################################################################################
# LIBRARY IMPORTING
##########################################################################################################

from tqdm import tqdm
import time
import os
import numpy as np
import matplotlib.pyplot as plt
import time
import subprocess

##########################################################################################################
# FUNCTION DEFINITION
##########################################################################################################

#Print a 'string' above the progress bar while it is still running
def print_tqdm(string):
    tqdm.write(string)

#Copy the folder from ./case to ./script when being in ./script
def caseCopy():
    os.chdir("..")
    os.system("cp -r ./baseCase ./scripts/case")
    os.chdir("scripts")
    
#Once the simulation is done, transfer the folders from case to the folder of each individual
def folderTransfer(analysisType,i,j):
    numFolder = []
    nonNumFolder = []
    for cFolder in os.listdir('case'):
        if cFolder != 'Gnuplotting.analyzed':
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

analysisType = 'steady' #'steady' (state) or 'transient' for folder transfer  
generations = 2
individuals = 2
values = np.array([[10,20],[30,40]])

#Initial linebreak to leave some space
print_tqdm('\n')

##########################################################################################################
# MAIN FUNCTION
##########################################################################################################

for i in range(generations):    
    #if there is not a folder for the current generation, this will create it
    if os.path.isdir("generation%i" %i) == False:
        os.system("mkdir generation%i" %i)
    
    #evaluate the function for each individual of the generation
    for j in tqdm(range(individuals),desc="{Generation %2.i}" %i):
        
        #if there is not a folder for the current individual, this will create it
        if os.path.isdir("generation%i/ind%i" %(i,j)) == False:
            os.system("mkdir generation%i/ind%i" %(i,j))

        #if there is not a folder for the current individual simulation, this will create it
        if os.path.isdir("generation%i/ind%i/sim" %(i,j)) == False:
            os.system("mkdir generation%i/ind%i/sim" %(i,j))
        
        #copy the preconfigured case
        caseCopy()
        
        #print the current state in the CLI
        print_tqdm('Simulation of inidividual %i' %j)
        
        #change a value in simulations to see change 
        os.system("sed -i 's/VARIABLE1/%i/g' ./case/0/U" %values[i,j])

        os.system("simpleFoam -case ./case > 'generation%i/ind%i/g%ie%i.txt' 2> 'generation%i/ind%i/error_g%ie%i.txt'" %(i,j,i,j,i,j,i,j))

        folderTransfer(analysisType,i,j)
        
        
        # If the error file is empty, this will erase the output of the solver after plotting the results
        if int(os.popen("du -h 'generation%i/ind%i/error_g%ie%i.txt'" %(i,j,i,j)).read()[0]) == 0: #i.e. error file is empty
            os.system("rm 'generation%i/ind%i/g%ie%i.txt'" %(i,j,i,j))
        # Otherwise print error
        else:
            print_tqdm('\033[0;33mError in simulation. Review logfile\033[0m') 
            
        os.system("rm -r case")
        
    print_tqdm('Evaluating fitness... \n')
    time.sleep(1)
    
#raise ValueError('\033[1;31mA very specific bad thing happened \033[0m') 