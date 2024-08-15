import math

n = int(input())

sqrtPi = (2*math.pi)**(1/2)
nPow = n**(n + (1/2))
ePowLower = math.e**(-n + (1/(12*n + 1)))
ePowUpper = math.e**(-n + (1/(12*n)))

print(sqrtPi * nPow * ePowLower)
print(sqrtPi * nPow * ePowUpper)