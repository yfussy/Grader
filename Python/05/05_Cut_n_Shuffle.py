deck = input().split()
operations = "".join(input().split())

for op in operations:
    firstHalf = deck[:len(deck)//2]
    secondHalf = deck[len(deck)//2:]
    if op == 'C':
        deck = secondHalf + firstHalf
    elif op == 'S':
        newDeck = []
        for i in range(len(deck)//2):
            newDeck.append(firstHalf[i])
            newDeck.append(secondHalf[i])
        deck = newDeck
print(" ".join(deck))