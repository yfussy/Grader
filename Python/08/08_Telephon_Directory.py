n = int(input())
nameTel = {}
telName = {}
for _ in range(n):
    first, last, tel = input().split()
    full_name = first + ' ' + last
    nameTel[full_name] = tel
    telName[tel] = full_name

m = int(input())
for _ in range(m):
    find = input()
    if find in nameTel:
        print(find + ' --> ' + nameTel[find])
    elif find in telName:
        print(find + ' --> ' + telName[find])
    else:
        print(find + ' --> Not found')