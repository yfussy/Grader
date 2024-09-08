def factor(N):
    factors = []
    k = 2
    i = 0
    while True:
        if N % k == 0:
            N //= k
            i += 1
            continue
        elif i or N == 1:
            factors.append([k, i])
            i = 0
        k += 1
        if k > N:
            break
    return factors

exec(input().strip())