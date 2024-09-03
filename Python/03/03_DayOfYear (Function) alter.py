def checkLeapYear(y):
    y -= 543
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    return False

def day_of_year(d, m, y):
    dayInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(m-1):
        d += dayInMonth[i]
        if (i == 1) & checkLeapYear(y):
            d += 1
    return d

exec(input()) 