dayInMonth = {
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

def checkLeapYear(y):
    y -= 543
    if (y % 4 == 0) & (y % 100 != 0):
        return True
    return False

def day_of_year(d, m, y):
    dayth = 0
    for i in range(1, m):
        if (i == 2) & checkLeapYear(y):
            dayth += 29
            continue
        dayth += dayInMonth[i]
    dayth += d
    return dayth

exec(input()) 