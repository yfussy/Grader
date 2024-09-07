delivDate = []
while True:
    deliv = input()
    if deliv == 'END':
        break
    id, typ, d, m ,y = deliv.split()
    err = f'Error: {id} {typ} {d} {m} {y} --> Invalid '
    d = int(d)
    m = int(m)
    y = int(y) - 543
    if y < 2015:
        print(err + 'year')
        continue
    mDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        mDays[1] += 1
    y += 543
    if m < 0 or m > 12:
        print(err + 'month')
        continue
    if d > mDays[m-1] or d <= 0:
        print(err + 'date')
        continue
    match typ:
        case 'E':
            d += 1
        case 'Q':
            d += 3
        case 'N':
            d += 7
        case 'F':
            d += 14
        case _:
            print(err + 'delivery type')
            continue
    if d > mDays[m-1]:
        d -= mDays[m-1]
        m += 1
        if m > 12:
            y += 1
            m = 1
    delivDate.append([y, m, d, id])
for y, m ,d, id in sorted(delivDate):
    print(f'{id}: delivered on {d}/{m}/{y}')