C, n = input().split()
C = float(C)
A = []
for _ in range(int(n)):
    full = int(C)
    deci = C - full
    A.append(full)
    if deci < 1e-10:
        break
    C = 1/deci
print(*A, sep=', ')