class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imag = b

    def __str__(self):
        real = self.real if self.real else ''
        imag = f'{abs(self.imag)}i'
        if abs(self.imag) == 1:
            imag = 'i'
        if self.imag == 0:
            imag = ''
            
        if imag and real:
            return f"{real}{'+' if self.imag > 0 else '-'}{imag}"
        elif real:
            return f'{real}'
        elif imag:
            return f"{'-' if self.imag < 0 else ''}{imag}"
        return '0'

    def __add__(self, rhs):
        real = self.real + rhs.real
        imag = self.imag + rhs.imag
        return Complex(real, imag)

    def __mul__(self, rhs):
        a, b, c, d = self.real, self.imag, rhs.real, rhs.imag
        real = (a * c) - (b * d)
        imag = (a * d) + (b * c)
        return Complex(real, imag)

    def __truediv__(self, rhs):
        a, b, c, d = self.real, self.imag, rhs.real, rhs.imag
        real = ((a * c) + (b * d))/(c**2 + d**2)
        imag = (-(a * d) + (b * c))/(c**2 + d**2)
        return Complex(real, imag)

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)