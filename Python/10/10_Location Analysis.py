n = int(input())
ids = {}
for _ in range(n):
    id, loc = input().split(':')
    loc = loc[1:].split(', ')
    ids[id] = loc
findId = input()
cities = ids[findId]
ids.pop(findId)
locs = list(ids.items())
found = False
for id,loc in locs:
    if set(loc) & set(cities):
        print(id)
        found = True

if not found:
    print('Not Found')