scores = list(map(float, input().split()))

min = scores[0]
max = scores[0]

for score in scores:
    if score < min:
        min = score
    if score > max:
        max = score

scores.remove(min)
scores.remove(max)

print(round(sum(scores)/2, 2))