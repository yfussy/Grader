import numpy as np

def mult_table(nrows, ncols):
    table = np.arange(1, ncols+1)
    mult = np.arange(1,nrows+1).reshape(nrows,1)
    return table * mult

exec(input().strip())