# Package importation
import numpy as np
import math
import random
import scipy.stats as stats
import optunity
from problemSetup import *
import sys

################################################################################
#                              FUNCTION DEFINITION                             # 
################################################################################
# This class will be used in the fastNonDominatedSorting to make a neat code
class Individual(object):
    p = []
    n = 0
    # Each individual will have p and n
    def __init__(self, p, n):
        self.p = p
        self.n = n


def prec_operator(P,Q):
    """Implementation of the dominance operator to sort a set of points.
    
    INPUTS:
    P:    first point (value in the function domain) with numpy.ndarray type
    Q:    second point (value in the function domain) with numpy.ndarray type
     
    OUTPUT:
    bool: True if P < Q and False if Q < P
    
    
    The dominance (precedant) operator returns True or False depending on the values 
    that the different functions have for each point. This follows the formal definition
    of the precedant operator: in order have a point dominating another, the values of 
    the functions should be smaller or equal for all objectives, having AT LEAST one for 
    which the values is strictly smaller than the dominated points 
    """
        
    # Number of variables
    var = P.shape[0]
    
    # Dimensions between p and q must match
    if var != Q.shape[0]:
        raise ValueError("P and Q dimensions don't match")
    
    # If all elements in P are smaller than those in Q, then P is dominating
    if np.sum(P < Q) == var:
        return True
    # Formal dominance-operator definition
    elif np.sum(np.logical_or(P < Q, P == Q)) == var and np.sum(P < Q) >= 1: 
        return True
    else:
        return False


def fastNonDominatedSort(P):
    """fast-non-dominated-sorting algorithm decribed in the NSGA-II paper
    
    INPUT:
    P:  point evaluations in the function space as a numpy.ndarray
    
    OUTPUT:
    PF: Pareto Front points in a list (number of PF) of numpy.ndarray (points)
    F:  index points in a list (number of PF) of numpy.ndarray (index)
    
    
    The function analyzes the value of the functions in the array P and sort the points 
    in Pareto Fronts, having that PF[0] contains the non dominated values in the set P, 
    PF[1] contains the values of the first dominated set, PF[1] the values of the second, 
    and so on. List F[] has the same idea of PF[] but containing the index of the points 
    instead of the true value of the point.
    """
    
    # Number of variables of the problem
    var = P.shape[1]
    # Possible solutions
    ps = P.shape[0] 
    ind = []
    # Pareto front list
    F = []
    # Let's create an empty array for the 1st Pareto front
    F1 = np.empty((0,1), float) # Just the index of the point will be stored

    for i in range(ps):
        # Dominated solutions for each p and its domination count n_p for the solution 
        S_p = np.empty((0,1), float) 
        n_p = 0
        for j in range(ps):
            # If p dominates q in all variables it will be smaller in all variables
            if prec_operator(P[i],P[j]): 
                S_p = np.append(S_p, j) # Add q to the set of solutions dominated by p
            elif prec_operator(P[j],P[i]):
                n_p += 1 # Increment the domination counter of p
        if n_p == 0: # p belongs to the first front
    #         p_rank = 1 
            F1 = np.append(F1, i) # Let's include the rank after the two main variables
        ind.append(Individual(S_p, n_p))
    # Store the first frontier in the frontiers list
    F.append(F1.astype(int))

    front = 0

    while len(F[front]) != 0:
        Q = np.empty((0,1), float) # Used to store the members of the next front
        for i in range(F[front].size): 
            for j in range(ind[int(F[front][i])].p.size):
                # Reduce the domination counter by 1
                ind[int(ind[int(F[front][i])].p[j])].n -= 1 
                # q belongs to the next front if its n == 0
                if ind[int(ind[int(F[front][i])].p[j])].n == 0: 
#                     q_rank = front + 2 
                    Q = np.append(Q, int(ind[int(F[front][i])].p[j]))
        front += 1
        F.append(Q.astype(int))

    # Let's create the values of the points instead index
    PF = []
    for i in range(front):
        PF.append(P[F[i].astype(int).tolist()])
        
    return PF, F


def crowdingDistanceAssignment(PF):
    """Assignment of a crowding distance value for a specific Pareto Front.
    
    INPUT:
    PF: specific Pareto Front values in the function space as numpy.ndarray
    
    OUTPUT:
    I:  crowding distance between points as a numpy.ndarray
    
    
    The implementation is based on the procedure proposed in the NSGA-II paper:
        - Assign a value in the extrema of infinity
        - Computes the crowding distance between the other points
        - Store the results following the same order as the points in PF
    """
    l = PF.shape[0] # Number of solutions in PF
    m = PF.shape[1] # Number of objective functions
    I = np.zeros((l,m)) # Preallocate distance
    for i in range(m):
        temp = PF[np.argsort(PF[:,i])] # Sort by using objective value m
        # Boundary points are selected as infinite so they will always be choosen
        I[np.argsort(PF[:,i])[0],i] = float('inf') 
        I[np.argsort(PF[:,i])[-1],i] = float('inf')
         # For the points that are not in the boundaries
        for j in range(1,l-1):
            I[np.argsort(PF[:,i])[j],i] = (temp[j+1,i] - temp[j-1,i])/(temp.max(axis=0)[i]-temp.min(axis=0)[i])  
        # Value normalization with 1 as maximum value only if it is bigger than 2
        if l > 2:
            I[:,i] = I[:,i]/np.max(I[I[:,i]!=np.inf,i])
            
    return I


def prec_n_operator(rank, crowd):
    """Implementation of the precedent_n operator to sort a set of points.
    
    INPUTS:
    rank:  ranking of the individuals as a numpy.ndarray 
    crowd: crowding distances stored in a numpy.ndarray
    
    OUTPUT:
    fObj:  returns a numpy.ndarray with the index of the sorted points (as integers)
    
    
    The implementation follows a close procedure to the one described in NSGA-II paper but 
    untie possible objective mismatches by using the mean to get the point located in the
    less populated area (bigger densities and bigger max(rank)-rank first)
    """
    
    # Let's invert the ranks to sort descending in all variables. Thus, the highest
    # the value of the new rank, the better Pareto front the point is located in.
    rank = max(rank) - rank

    # Descending sorted matrix taking into account rank and mean of crowding distances
    obj = np.flipud(np.lexsort(((crowd[:,0]+crowd[:,1])/2,rank)))
    # Before returning the index list, check if there is no repeated number
    if any(np.unique(obj, return_counts=True)[1] != 1):
        # If there it is, return a warning
        warnings.warn("Repeated numbers in the prec_n_operator output")
    # Return the solution
    return obj.astype(int)


def preSelection(P, Q, funEvalP, funEvalQ):
    """Selection based on the mixing of parents and offsprings 
    
    INPUTS:
    P:        parents [p-1] (in parameter space) as a numpy.ndarray
    Q:        offspring [p] (in parameter space) as a numpy.ndarray
    funEvalP: parents (in function space) as a numpy.ndarray
    funEvalQ: offsprings (in function space) as a numpy.ndarray
    
    OUTPUT:
    newP:     new population ready for selection, crossover...


    This function mix the population of parents (generation [p-1]) and offsprings 
    (generation [p]). Then it is sorted following the non-dominated sorting, taking 
    the whole fronts when they fill completely the new population size. Once the next
    front doesn't fit into the new population vector, it is sorted by crowding distance
    picking the ones that have higher values of crowding distances (and recomputing the
    crowding distance each time an individual is taken out the Pareto front)
    """
    
    N = len(P)
    # Combine parent and offspring population
    R = np.concatenate((P,Q))
    funEvalR = np.concatenate((funEvalP,funEvalQ))
    
    # Let's sort all the nondominated fronts of R
    PF, F = fastNonDominatedSort(funEvalR)
    
    # Store the Pareto Front number of each one of the P points
    PFnumber = np.zeros(len(np.concatenate(PF))) 
    count = 0
    for pfn in range(len(F)):
        for pfe in range(len(F[pfn])):
            PFnumber[F[pfn][pfe].astype(int)] = pfn
            count += 1

    # New generation should have the same number of individuals as the previous one
    newP = np.zeros((N, 7)) # coord1 - coord2 - fun1 - fun2 - rank - crowd1 -crowd2

    i = 0
    nPcount = 0
    
    # Until the parent population is filled
    while np.sum(newP.any(axis=1)) + len(F[i]) <= N:
        # Calculate the crowding-distance for F[i]
        crowdDA = crowdingDistanceAssignment(funEvalR[F[i]])
        # Include the i-th nondominated front in the parent population
        for j in range(len(F[i])):
            newP[nPcount,:] = np.hstack((R[F[i][j],:], funEvalR[F[i][j],:], PFnumber[F[i][j]], crowdDA[j,:]))
            nPcount += 1
        # Check the next front for inclusion
        i += 1   
        
    # Compute the crowding distance for the next F[i] 
    crowdDA = crowdingDistanceAssignment(funEvalR[F[i]])
    # Sort in descensing order using the prec_n operator
    sortedFl = prec_n_operator(PFnumber[F[i]],crowdingDistanceAssignment(funEvalR[F[i]]))
    # sortedFl = prec_n_operator(PFnumber[F[i]],crowdDA)

    # Choose the first (N-len(F[i])) elements of F[i]
    stillEmpty = N - np.sum(newP.any(axis=1))
    
    # Go through the elements that may be chosen
    for j in sortedFl[0:stillEmpty]:
        newP[nPcount,:] = np.hstack((R[F[i][j],:], funEvalR[F[i][j],:], PFnumber[F[i][j]], crowdDA[j,:]))
        nPcount += 1
   
    # Return the new population ready to selection
    return newP


def binaryTournament(rank, crowd):
    """Binary tournament selection process based on the precedent_n operator
    
    INPUTS:
    rank:  rank (Pareto front number) in which points are located
    crowd: crowding distance of the points that will be confronted
    
    OUTPUT:
    index: index of the winning individual
    
    
    The basic operation that this function performs is the selection of two
    random individuals from a list, comparison of its rank and crowding 
    distance and select the winner based on the precedent_n operator
    """
    
    # Get the size of the population
    N = rank.shape[0]
    
    # Dimensions between rank and crowd must match
    if N != crowd.shape[0]:
        raise ValueError("Rank and crowd dimensions don't match")
    
    # Create an array with the N possible index positions
    indx = np.linspace(0,N-1,N).astype(int)
    
    # Get two random positions for each one of the contestants
    cntA = np.random.choice(indx)
    cntB = np.random.choice(indx)
    
    # Avoid mutual participation in the tournament
    while cntA == cntB:
        cntA = np.random.choice(indx)
        cntB = np.random.choice(indx)   
            
    # List contestants, its rank and its crowding distance
    cntList = np.array([cntA,cntB])
    cntRank = np.array([rank[cntA],rank[cntB]])
    cntCrowd = np.array([crowd[cntA],crowd[cntB]])
    
    # Apply the dominance_n operator to get the winner
    winner = prec_n_operator(cntRank, cntCrowd)

    # The winner is the element 0 from the prec_n operation
    return cntList[winner == 0][0]


def crossover(ind1, ind2, d, n_c, line, SBX):
    """Crossover of two individuals with intermediate or linear recombination
    
    INPUTS:
    ind1: first individual as numpy.ndarray
    ind2: second individual as numpy.ndarray
    d:    spacing area of possible offspring location
    n_c:  distribution index (the higher value, the closer to the parents)
    line: True for linear recombination, False for intermediate/SBX crossover
    SBX:  True for simulated binary crossover, False for intermediate/linear crossover
    
    OUTPUTS:
    off:  new individual as numpy.ndarray
    
    SBX (Simulated Binary Crossover) is based on the binary crossover operator used for 
    binary encoded problems, but adapted for real variable cases. The algorithm is 
    described in detailed in the Deb's paper:
    https://pdfs.semanticscholar.org/b8ee/6b68520ae0291075cb1408046a7dff9dd9ad.pdf
    This crossover method will return two offspring instead of just one, having that it
    should loop over just N/2 times (where N is the population size)
    
    Linear crossover is based on:
                         x_o = x_1 * a_i + x_2 * (1 - a_i)
    to get new individuals. The difference between linear and intermediate recombination
    is that for intermediate recombination the value of a_i is computed for each variable 
    while for linear recombination a_i will be the same for all variables. a_i is chosen 
    randomly from the interval [-d,1+d] where d is the input value. The most common value
    of d is 0.25 because it ensures diversity (at least statistically).
    
    Finally blend crossover is based on a range given by [-d, 1+d] to move the parents 
    points values in a fixed range, having a square (two variable case) of possible 
    offspring values centered in the parents locations
    """
    
    # Analyze the type of crossover that will be performed
    if np.sum([line, SBX]) == 2:
        raise RuntimeError('Incorrect crossover type selection')
    
    # Preallocation of space for the offspring as the parents
    off = np.zeros_like(ind1)
     
    # Simulated binary crossover (SBX)
    if SBX:
        # Preallocation of space for the second offspring
        off2 = np.zeros_like(ind1)
        # Random number computation and beta parameter
        u = np.random.rand() 
        if u <= 0.5:
            beta = (2*u)**(1/(n_c+1))
        else:
            beta = (1/(2*(1-u)))**(1/(n_c+1))
        # Offspring computation
        off = 0.5*((1+beta)*ind1+(1-beta)*ind2)
        off2 = 0.5*((1-beta)*ind1+(1+beta)*ind2)
        return off, off2
    # Linear recombination
    elif line:
        # Generate one a_i for all possible variables of the individual
        a_i = np.random.uniform(-d, 1+d)
        for i in range(ind1.shape[0]):
            # Mutate each variable with the same a_i
            off[i] = ind1[i]*a_i + ind2[i]*(1 - a_i)
        return off
    # Intermediate recombination / blend crossover
    else:
        for i in range(ind1.shape[0]):
            # For each variable, compute a random a_i and mutate
            a_i = np.random.uniform(-d, 1+d)
            off[i] = ind1[i]*a_i + ind2[i]*(1 - a_i)
        return off


def mutation(ind, r, domain, k, n_m, normalDist, poly):
    """Mutates the individual with uniform, normal or polynomial distribution
    
    INPUTS:
    ind:        individual as numpy.ndarray
    r:          range of mutation [0-1] multiplied by the domain
    domain:     search domain for each variables of ind as numpy.ndarray
                following (x_min, x_max, y_mix, y_max)
    k:          mutation precision for a_i = 2^(u_i * k)
    n_m:        distribution index 
    normalDist: True for normal mutation, False for uniform/polynomial
    poly:       True for polynomial mutation, False for uniform/random
    
    OUTPUTS:
    mInd:       mutated individual as numpy.ndarray
    
    
    The mutation is defined by:
            x_m = x_i + s_i * r * domain * 2^(u_i * k)
    where the values depend on the different input parameters. Common ranges
    for those inputs are:
        - r = [1e-1,1e-6]
        - k = [4-20]
    """
    
    # Analyze the type of crossover that will be performed
    if np.sum([normalDist, poly]) == 2:
        raise RuntimeError('Incorrect mutation type selection')
    
    # Preallocation of space for the mutated individuals
    mInd = np.zeros_like(ind)
    
    # Random sign vector with positive and negative signs 
    s_i = [1.,-1.]
    
    # Domain range set length of search ranges
    sDomain = np.array([domain[1]-domain[0],domain[3]-domain[2]])
    
    if poly:
        # Perform mutation for all variables
        for j in range(ind.shape[0]):
            # Get parameter u from random distribution
            u = np.random.rand()
            # Operate based on the value of u
            if u <= 0.5:
                delta = (2*u)**(1/(1+n_m)) - 1
                mInd[j] = ind[j] + delta*(ind[j] - domain[2*j])
            elif u > 0.5:
                delta = 1 - (2*(1-u))**(1/(1+n_m))
                mInd[j] = ind[j] + delta*(domain[2*j+1] - ind[j])
    elif normalDist:
        # Although a truncated normal distribution in [-1, 1] may be used, to maximize
        # performance a normal distribution will be used (correcting values afterwards)
#         mInd[i] = ind[i] + r*domain[i]*stats.truncnorm(-2, 2, loc=0, scale=0.5).rvs(1) 
        mInd = ind + r*sDomain*np.random.normal(0.0, 0.25, 2)
    else:
        # Otherwise an uniform random distribution will be used
        mInd = ind + np.random.choice(s_i,2)*r*sDomain*2**(-np.random.rand(2)*k)

    return mInd

################################################################################
#                                   MAIN BODY                                  # 
################################################################################
# Get the current generation from the input
gen = int(sys.argv[1])
# Set crossover probability with a fixed value
crossProb = 0.9


# If it is the first generation it must be compared against itself
if gen == 0:
	# Get the values of the population, both search and function space
	PfE = np.genfromtxt('./data/gen%i.txt' %gen, delimiter=',')
	# True size of the populations is half the size of the first generation
	N = int(len(PfE)/2)
	# Selection of the parents for the first generation
	parents = preSelection(PfE[0:N,0:2],PfE[N:2*N,0:2],PfE[0:N,2:4],PfE[N:2*N,2:4])
# Otherwise, compare with the parents (previous generation)
else:
	# Get the values of the paretns, both search and function space
	PfEparents = np.genfromtxt('./data/gen%i.txt' %(gen-1), delimiter=',')
	# Get the values of the offsprint, both search and function space
	PfEoffspring = np.genfromtxt('./data/gen%i.txt' %(gen), delimiter=',')
	# Size of the population
	N = int(len(PfEoffspring))
	# Selection of the parents for the first generation
	parents = preSelection(PfEparents[:,0:2],PfEoffspring[:,0:2],PfEparents[:,2:4],PfEoffspring[:,2:4])


# Get the size of the mating pool
poolSize = round(N/2)

# Create a list to store the index of the better individuals
pool = [] 

# Filling the mating pool with binary tournament 
for i in range(poolSize):

    # Binary tournament based on the preselected individuals 
    # and its values of Pareto Front rank and its crowding distance
    chosenInd = binaryTournament(parents[:,4], parents[:,5:7])

    # The first element will never be on the list
    if i == 0:
        pool.append(chosenInd)
    # For the following individuals
    else:
        # Test if the individual is on the pool
        while int(chosenInd) in pool:
            # And make a binary tournament again if it already is
            chosenInd = binaryTournament(parents[:,4], parents[:,5:7])
        # Appending once the chosen individual is not in the pool
        pool.append(chosenInd)

# Preallocation of space for the children
children = np.zeros([N,2])

# Looping over the whole length of the generation
for i in range(N):
    # If the random chosen value is below the crossover probability
    if np.random.rand(1) < crossProb:

        # Selection of two points with the binary tournament
        pt1 = parents[np.random.choice(pool),0:2]
        pt2 = parents[np.random.choice(pool),0:2]

        # Let's prevent self point crossover
        while all(pt1 == pt2):
            pt1 = parents[np.random.choice(pool),0:2]
            pt2 = parents[np.random.choice(pool),0:2]

        # Using simulated binary crossover with n_c = 20
        children[i,:] = crossover(pt1, pt2, 0.0, 20, False, True)[0]

        # Applying a smaller mutation to the latest created individual
        children[i,:] = mutation(pt1, 0.2, 
                                  np.array([x_low, x_high, y_low, y_high]), 
                                 6, 50, False, True)

    # If it is not crossover, then it must be mutation 
    else:

        # Selection of one point with the binary tournament
        pt1 = parents[np.random.choice(pool),0:2]

        # Using polynomial mutation with n_m = 20
        children[i,:] = mutation(pt1, 0.2, 
                                  np.array([x_low, x_high, y_low, y_high]), 
                                 6, 20, False, True)

    # Constrained values will be replaced, given new random numbers in its places
    while sum(constrainedPts(children, const, constVal, compMode)) != 0:
        # The points where the constraints are not fulfilled ...
        boolMat = constrainedPts(children, const, constVal, compMode)
        # ... are replaced with random numbers
        for i in np.argwhere(boolMat == True):
            children[i,:] = np.array([x_low+np.random.rand(1)*(x_high-x_low),
                                      y_low+np.random.rand(1)*(y_high-y_low)]).T

# Children matrix will be saved as the execution data for next generation
np.savetxt('./gen%i/popx%i' %(gen+1, gen+1), children[:,0], fmt='%.8f', delimiter=',')
np.savetxt('./gen%i/popy%i' %(gen+1, gen+1), children[:,1], fmt='%.8f', delimiter=',')