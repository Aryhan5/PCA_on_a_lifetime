'''
Agrégation SLAM/CML les données. Génération d'un objet 3D (unity ou unreal), Arcore ?
'''

import numpy as np

def relative_distance(positions):
    #create a distance matrix

    n = np.size(positions)
    m = np.zeros(n,n)

    for i in n:
        for j in n:
            m[i][j] = np.linalg.norm(positions.i, positions.j)
    
    return m

def transition_flow(distances):
    #calculate likehood of individial transition giving relative distance

    '''
        for each element in the matrix
            element = 1/(element^2)
    '''
    return

def transition_probabilities(pipeflow):
    #creation of a probababilistic transition table

    #probable use of pagerank
    return

def treshold(probabilities):
    #lowpass probabilites to improve visibility in rendering
    return


