def spiral_square(n):
    s = [[1]]
    num = 1
    r = 1
    c = 1
    for i in range(1, ((n+1)//2)):
        lim = 2*(i+1) - 2
        s = [[0 for _ in range(lim+1)]] + [[0] + layer + [0] for layer in s] + [[0 for _ in range(lim+1)]]
        dr = 0
        dc = 1
        for _ in range(8*i):
            num += 1
            if dc:
                if c == lim:
                    dc = 0
                    dr = -1
                elif c == 0:
                    dc = 0
                    dr = 1
            elif dr:
                if r == lim:
                    dc = 1
                    dr = 0
                elif r == 0:
                    dc = -1
                    dr = 0
            c += dc
            r += dr
            s[r][c] = num
        r += 1
        c += 1
    return s     

def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip())