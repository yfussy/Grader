class Card:
    valPrior = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
    suitPrior = ['club', 'diamond', 'heart', 'spade']
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.prior = (self.valPrior.index(value), self.suitPrior.index(suit))

    def __str__(self):
        return f'({self.value} {self.suit})'
    
    def next1(self):
        curValPrior, curSuitPrior = self.prior
        if curSuitPrior == len(self.suitPrior) - 1:
            if curValPrior == len(self.valPrior) - 1:
                return Card(self.valPrior[0], self.suitPrior[0])
            return Card(self.valPrior[curValPrior + 1], self.suitPrior[0])
        return Card(self.value, self.suitPrior[curSuitPrior + 1])
    
    def next2(self):
        nextCard = self.next1()
        self.__init__(nextCard.value, nextCard.suit)
    
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])