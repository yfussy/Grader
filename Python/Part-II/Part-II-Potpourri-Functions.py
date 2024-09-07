import math

def convex_polygon_area(p):
    centroid = [sum([x for x,_ in p])/len(p), sum([y for _,y in p])/len(p)]
    angles = [math.atan2(y-centroid[1],x-centroid[0]) for x,y in p]
    coordAng = dict(zip(angles, p))
    ordered = [coordAng[ang] for ang in sorted(coordAng)]

    area = 0
    for i in range(len(ordered)):
        x1, y1 = ordered[i]
        x2, y2 = ordered[(i+1)%len(ordered)]
        area += (x1 * y2) - (x2 * y1)
    return area * 0.5

def is_heterogram(s):
    seen = []
    for c in s.lower():
        if c in seen and c.isalpha():
            return False
        else:
            seen.append(c)
    return True

def replace_ignorecase(s, a, b):
    t = ''
    prev = 0
    while True:
        check = s.lower().find(a.lower(), prev)
        if check == -1:
            t += s[prev:]
            break
        t += s[prev:check] + b
        prev = check + len(a)
    return t

def top3(votes):
    invert = [(-score, name) for name, score in votes.items()]
    return [name for _, name in sorted(invert)][:3]

for k in range(2):
    exec(input().strip())