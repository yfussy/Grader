n = int(input())
firstL = {}
lastF = {}
for _ in range(n):
    first, last = input().split()
    firstL[first] = last
    lastF[last] = first
m = int(input())
for _ in range(m):
    find = input()
    if find in firstL:
        print(firstL[find])
    elif find in lastF:
        print(lastF[find])
    else:
        print('Not found')