def pattern1(nrows, ncols):
    table = [[0]*ncols for _ in range(nrows)]
    num = 1
    for i in range(nrows):
        for j in range(ncols):
            table[i][j] = num
            num += 1
    return table

def pattern2(nrows, ncols):
    table = [[0]*ncols for _ in range(nrows)]
    num = 1
    for i in range(ncols):
        for j in range(nrows):
            table[j][i] = num
            num += 1
    return table

def pattern3(N):
    table = [[0]*N for _ in range(N)]
    num = 1
    for i in range(N):
        for j in range(N-i):
            table[i][i+j] = num
            num += 1
    return table

def pattern4(N):
    table = [[0]*N for _ in range(N)]
    num = 1
    for i in range(N):
        for j in range(i,-1,-1):
            table[j][i] = num
            num += 1
    return table

def pattern5(N):
    table = [[0]*N for _ in range(N)]
    num = 1
    for i in range(N):
        for j in range(N-i):
            table[j][i+j] = num
            num += 1
    return table

def pattern6(N):
    table = [[0]*N for _ in range(N)]
    num = 1
    for i in range(N):
        if i % 2 != 0:
            for j in range(N-1, i-1,-1):
                table[j-i][j] = num
                num += 1
        else:
            for j in range(N-i):
                table[j][i+j] = num
                num += 1
    return table

exec(input().strip()) 