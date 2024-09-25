import numpy as np

def toCelsius(f):
    return (f - 32)*5/9

def BMI(wh):
    w = wh[:,0]
    h = wh[:,1] / 100
    return w/h**2

def distanceTo(p, Points):
    disSquare = (p - Points)**2
    return np.sqrt(np.sum(disSquare, axis=1))

exec(input().strip())