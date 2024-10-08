def read_matrix():
    m = []
    nrows = int(input())
    for _ in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m

def mult_c(c, A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= c
    return A

def mult(A, B):
    C = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            ans = 0
            for k in range(len(A[0])):
                ans += A[i][k] * B[k][j]
            C[i][j] = ans
    return C

exec(input().strip())