def distance1 (x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def distance2(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def distance3(c1, c2):
    overlap = False
    if distance2(c1, c2) <= c1[2] + c2[2]:
        overlap = True

    return distance2(c1, c2), overlap

def perimeter(points):
    p = 0
    points.append(points[0])
    for i in range(len(points)-1):
        p += distance2(points[i], points[i+1])
    return p

exec(input().strip())