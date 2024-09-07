cards = {
    'A': 1,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13
}

sets = {
    'C': 1,
    'D': 2,
    'H': 3,
    'S': 4
}

deck = input()
integral = ''
for i in range(0,len(deck)-2, 2):
    firstCard = deck[i:i+2]
    secondCard = deck[i+2:i+4]
    dif = cards[firstCard[0]] - cards[secondCard[0]]
    if dif:
        integral += '+' if dif > 0 else ''
        integral += str(dif)
    else:
        dif = sets[firstCard[1]] - sets[secondCard[1]]
        integral += '+' if dif > 0 else ''
        integral += str(dif)
print(integral)