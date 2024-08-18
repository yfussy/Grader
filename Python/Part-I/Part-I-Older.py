MONTHS = ["January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

n1, m1, d1, y1 = input().split()
n2, m2, d2, y2 = input().split()

if int(y1) == int(y2):
    if m1 == m2:
        if d1 == d2:
            print(n1, n2)
        elif int(d1[:-1]) > int(d2[:-1]):
            print(n2)
        else:
            print(n1)
    elif MONTHS.index(m1) > MONTHS.index(m2):
        print(n2)
    else:
        print(n1)
elif int(y1) > int(y2):
    print(n2)
else:
    print(n1)