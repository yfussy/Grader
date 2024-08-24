numList = sorted(list(set(map(int, input().split()))))

print(len(numList))
if len(numList) > 10:
    numList = numList[:10]
print(numList)