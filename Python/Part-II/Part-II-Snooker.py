logBook = []
ballScore = {
    'R': 1,
    'Y': 2,
    'G': 3,
    'W': 4,
    'B': 5,
    'P': 6,
    'K': 7
}
while True:
    log = input()
    logBook.append(log)
    if log[1] == 'K':
        break

scores = [0,0]
for log in logBook:
    for play in log[1:]:
        if play == 'X':
            continue
        scores[int(log[0])-1] += ballScore[play]

print(' '.join(map(str, scores)))
if scores[0] == scores[1]:
    print('Tie')
else:
    print(f'Player {scores.index(max(scores)) + 1} wins')