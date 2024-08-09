import math

a,b,c = input().split(',')

decimalNoRepeat = int(a+b+c) - int(a+b)
fraction = (10**len(b+c)) - (10**len(b))

numerator = int(decimalNoRepeat // math.gcd(decimalNoRepeat, fraction))
denominator = int(fraction // math.gcd(decimalNoRepeat, fraction))

print(f'{numerator} / {denominator}')