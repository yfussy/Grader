import numpy as np
def peak_indexes(x):
    lhs = x[1:-1] > x[:-2]
    rhs = x[1:-1] > x[2:]
    peaks = lhs & rhs
    return np.arange(1,len(x)-1)[peaks]
def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")

exec(input().strip())