dir, year = input().split()
fin = open(dir, 'r')
data = fin.readline().split()
minScore = 0
maxScore = 0
scores = []
while len(data) != 0:
    sid, score = data
    score = float(score)
    if sid[:2] == year[-2:]:
        minScore = min(score, minScore) if minScore != 0 else score
        maxScore = max(score, maxScore)
        scores.append(score)
    data = fin.readline().split()
if len(scores) == 0:
    print('No data')
else:
    meanScore = sum(scores)/len(scores)
    print(minScore, maxScore, meanScore)