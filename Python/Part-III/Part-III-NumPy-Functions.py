import numpy as np

def eq(A,B,p):
    dif = A - B
    filtPercent = len(dif[dif == 0])/np.prod(A.shape)*100
    if filtPercent >= p:
        return True
    return False

def closest_point_indexes(points, p):
    difSq = (points - p)**2
    distance = np.sum(difSq, axis=1)**0.5
    pos = np.arange(distance.shape[0])
    return pos[distance == np.min(distance)]

def number_of_inversions(A):
    dup, ind = np.triu_indices(len(A), k=1)
    pair = A[dup] > A[ind]
    return np.sum(pair)
    
exec(input().strip())