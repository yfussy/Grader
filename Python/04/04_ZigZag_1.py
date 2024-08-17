n = int(input())
xList = []
yList = []
for i in range(n):
    x, y = list(map(int, input().split()))
    xList.append(x)
    yList.append(y)
operation = 1 if str(input()) == 'Zig-Zag' else -1

minLine = xList[0] if operation == 1 else yList[0]
maxLine = yList[0] if operation == 1 else xList[0]
for i in range(1, n):
    minLine = min(minLine, yList[i] if operation == 1 else xList[i])
    maxLine = max(maxLine, xList[i] if operation == 1 else yList[i])
    operation *= -1

print(minLine, maxLine)