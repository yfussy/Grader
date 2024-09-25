import numpy as np
def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    totalScore = np.sum(data[:,1:]*weight, axis=1)
    meanScore = sum(totalScore)/data.shape[0]
    lowerMean = data[:,0][totalScore < meanScore]
    if lowerMean.size != 0:
        print(', '.join([str(e) for e in lowerMean]))
    else:
        print('None')

exec(input().strip())