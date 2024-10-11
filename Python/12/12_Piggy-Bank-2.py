class piggybank:
    def __init__(self):
        self.coins = {}
    
    def add(self, v, n):
        if sum(self.coins.values()) + n > 100:
            return False
        v = float(v)
        if v in self.coins:
            self.coins[v] += n
        else:
            self.coins[v] = n
        return True
    
    def __float__(self):
        money = 0.0
        for coin, n in self.coins.items():
            money += coin*n
        return money
    
    def __str__(self):
        return str(dict(sorted(self.coins.items()))).replace(': ', ':')
        
    
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)