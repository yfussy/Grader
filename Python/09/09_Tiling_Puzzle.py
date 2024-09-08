def row_number(t, e):
    for l in t:
        if e in l:
            return t.index(l)

def flatten(t):
    lint = [] 
    for l in t:
        for num in l:
            if num:
                lint.append(num)
    return lint

def inversions(x):
    n = 0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] > x[j]:
                n += 1
    return n

def solvable(t):
    inversionIsEven = inversions(flatten(t)) % 2 == 0
    zeroRowIsEven = row_number(t, 0) % 2 == 0
    rowIsEven = len(t) % 2 != 0
    if rowIsEven and inversionIsEven:
        return True
    if inversionIsEven ^ zeroRowIsEven:
        return True     
    return False

exec(input().strip())