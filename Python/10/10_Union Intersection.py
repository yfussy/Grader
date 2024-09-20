n = int(input())
sets = []
for _ in range(n):
    sets.append(set(input().split(' ')))
if sets:
    print(len(set.union(*sets)))
    print(len(set.intersection(*sets)))
else:
    print(0)
    print(0)