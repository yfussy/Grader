d = int(input())
m = int(input())
y = int(input())

dayInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
y -= 543

for i in range(m-1):
    d += dayInMonth[i]
    if i == 1 and ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)):
        d += 1

print(d)