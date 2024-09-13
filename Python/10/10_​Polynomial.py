def add_poly(p1, p2):
    p1 = {i:cf for cf, i in p1}
    for cf, i in p2:
        if i in p1:
            p1[i] += cf
            if p1[i] == 0:
                p1.pop(i)
        else:
            p1[i] = cf
    return [(cf, i) for i, cf in sorted(p1.items(), reverse=True)]

def mult_poly(p1, p2):
    mult1 = []
    for cf1, i1 in p1:
        for cf2, i2 in p2:
            mult1 = add_poly([(cf1*cf2, i1+i2)], mult1)
    return mult1

for i in range(3):
    exec(input().strip())