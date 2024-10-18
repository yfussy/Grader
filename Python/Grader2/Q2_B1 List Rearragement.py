D = [int(e) for e in input().split()]
x = 0
R = []
for p in sorted(D):
    x += p    
    i = x%len(D)
    R.append(D[i])
    D.pop(i)
print(*R, sep=' ')