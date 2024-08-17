a = float(input())
L = 0
U = 0
tenFloorDiv = a

while tenFloorDiv:
    tenFloorDiv = tenFloorDiv//10
    U += 1

x = (L + U) / 2

while abs(a - (10**x)) > 10**(-10) * max(a, 10**x):
    x = (L + U) / 2
    if 10**x > a:
        U = x
    elif 10**x < a:
        L = x
    else:
        break

print(round(x, 6))