date, p, n, sm = input().split()
d, m, y = [int(e) for e in date.split('/')]
p = int(p)
n = int(n)
sm = int(sm)
for i in range(n):
    i = (i%4) + 1
    if sm == m:
        i += 1
    p += p*(i/1200)
    sm = (sm%12) + 1
print(round(p,2))