wins = int(input())
m = 0
scores  = [0, 0]
gameRule = {
    'R': 'S',
    'P': 'R',
    'S': 'P'
}
winner = 0
while m < 3 * wins:
    p1, p2 = input().split()
    if p1 == p2:
        m += 1
        continue
    elif p2 in gameRule[p1]:
        scores[0] += 1
        m += 1
    else:
        scores[1] += 1
        m += 1
    if wins in scores:
        winner = scores.index(max(scores[0], scores[1])) + 1
        break
print(' '.join(list(map(str, scores))))
print(f'Player {winner} wins' if winner else 'Tie')