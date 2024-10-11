class Card:
    cardVal = {
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 1,
        '2': 2
    }

    cardPrior = [key for key in cardVal.keys()]
    suitPrior = ['club', 'diamond', 'heart', 'spade']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f'({self.value} {self.suit})'
    
    def getScore(self):
        return self.cardVal[self.value]
    
    def sum(self, other):
        return (self.getScore() + other.getScore()) % 10
    
    def __lt__(self, rhs):
        if self.value == rhs.value:
            selfPrior = self.suitPrior.index(self.suit)
            rhsPrior = self.suitPrior.index(rhs.suit)
        else:
            selfPrior = self.cardPrior.index(self.value)
            rhsPrior = self.cardPrior.index(rhs.value)
        return selfPrior < rhsPrior

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])