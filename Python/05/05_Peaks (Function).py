def peaks(x):
    prev = x[0]
    peak = []
    inPeak = False
    for i, point in enumerate(x):
        if inPeak:
            if point >= x[peak[-1]]:
                peak.pop()
            inPeak = False

        if point > prev:
            if i == len(x) - 1:
                break
            peak.append(i)
            inPeak = True
        prev = point
    return peak
exec(input())