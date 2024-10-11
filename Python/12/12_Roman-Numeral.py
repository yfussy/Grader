class roman:
    romanNum = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    numRoman = {n: r for r,n in reversed(romanNum.items())}
    reFormat = {
        'IIII': 'IV',
        'VIIII': 'IX',
        'XXXX': 'XL',
        'LXXXX': 'XC',
        'CCCC': 'CD',
        'DCCCC': 'CM'
    }

    def __init__(self, r):
        self.r = r
    
    def __int__(self):
        n = 0
        prev = ''
        for s in self.r:
            n += self.romanNum[s]
            match s:
                case 'V' | 'X':
                    if prev == 'I':
                        n -= 2
                case 'L' | 'C':
                    if prev == 'X':
                        n -= 20
                case 'D' | 'M':
                    if prev == 'C':
                        n -= 200
            prev = s
        return n
    
    def __str__(self):
        for i in range(len(self.r)-4):
            looking = self.r[i:i+5]
            if looking in self.reFormat:
                self.r = self.r[:i] + self.reFormat[looking] + self.r[i+5:]
        return self.r
    
    def __lt__(self, rhs):
        return int(self) < int(rhs)
    
    def __add__(self, rhs):
        new = int(self) + int(rhs)
        newRoman = ''
        for num, ro in self.numRoman.items():
            if new//num > 0:
                n = new//num
                for _ in range(n):
                    newRoman += self.numRoman[num]
                new -= n*num
        return roman(newRoman)


t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))