scores = list(map(float, input().split()))
scores.sort()
print(round(sum(scores[1:3])/2, 2))