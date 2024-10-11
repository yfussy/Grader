class piggybank:
    def __init__(self):
        self.tens = 0 
        self.fives = 0 
        self.twos = 0 
        self.ones = 0 

    def add1(self, n):
        self.ones += n
    
    def add2(self, n):
        self.twos += n
    
    def add5(self, n):
        self.fives += n
    
    def add10(self, n):
        self.tens += n

    def __int__(self):
        return self.tens*10 + self.fives*5 + self.twos*2 + self.ones
    
    def __lt__(self, rhs):
        return int(self) < int(rhs)
    
    def __str__(self):
        return '{' + f'1:{self.ones}, 2:{self.twos}, 5:{self.fives}, 10:{self.tens}' + '}'

cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)