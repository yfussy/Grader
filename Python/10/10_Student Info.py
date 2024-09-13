n = int(input())
names = []
for _ in range(n):
    names.append(input().split())
filtering = input().split()
for find in filtering:
    findIndex = {}
    names = [name for name in names if find in name]
    for name in names:
        currIndex = name.index(find)
        if currIndex in findIndex:
            findIndex[currIndex] += 1
        else:
            findIndex[currIndex] = 1
    findIndex = sorted([(amt, index) for index, amt in findIndex.items()], reverse=True)
    names = [name for name in names if name.index(find) == findIndex[0][1]]

if names:
    for name in sorted(names):
        print(' '.join(name))
else:
    print('Not Found')