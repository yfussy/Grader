bd, bm, by, d, m, y = list(map(int, input().split()))

days31 = [1, 3, 5, 7, 8, 10, 12]
days30 = [4, 6, 9, 11]


def isLeapYear(y):
    y -= 543
    if y % 4 == 0:
        if y % 100 == 0:
            return False
        return True
    return False

def monthDays(m, y):
    if m in days31:
        return 31
    elif m in days30:
        return 30
    else:
        if isLeapYear(y):
            return 29
        else:
            return 28

def daysLeft(m, y, color):
    d = 0
    if color == "red":
        settings = [12, m, -1]
    else:
        settings = [1, m, 1]
    for i in range(settings[0], settings[1], settings[2]):
        d += monthDays(i, y)
    return d
        
redDays = monthDays(bm, by) - bd + daysLeft(bm, by, "red") + 1
blueDays = d + daysLeft(m, y, "blue") - 1
print(redDays, blueDays)
