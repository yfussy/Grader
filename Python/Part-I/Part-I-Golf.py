import math

pars = 0
strokes = 0
newStrokes = 0
for i in range(9):
    par, stroke, consider = list(map(int, input().split()))
    if consider:
        newStrokes += min(par+2, stroke)
    pars += par
    strokes += stroke
handicap = math.floor(0.8 * ((1.5 * newStrokes) - pars))
scores = strokes - handicap
print(strokes)
print(handicap)
print(scores)