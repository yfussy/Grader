d = int(input())
m = int(input())
y = int(input())

daysInMonth = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

for i in range(1, m, 1):
    if (y-543) % 4 == 0 and i == 2:
        if (y-543) % 100 == 0:
            if (y-543) % 400 == 0:
                d += 1
        else:
            d += 1
    d += daysInMonth[i]

print(d)