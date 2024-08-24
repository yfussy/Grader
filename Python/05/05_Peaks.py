numList = list(map(int, input().split()))
prev = numList[0]
peak = []
inPeak = False
for i, point in enumerate(numList):
    if inPeak:
        if point >= numList[peak[-1]]:
            peak.pop()
        inPeak = False

    if point > prev:
        if i == len(numList) - 1:
            break
        peak.append(i)
        inPeak = True
    prev = point
print(len(peak))