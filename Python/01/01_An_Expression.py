import math

fac = math.factorial(10)/8**8
loge = math.log(9.7)
pow = 7/math.sqrt(71) - math.sin(math.radians(40))
denom = 1.2**(2.3**(1/3))
ans = (math.pi - fac + loge**pow)/denom

print(round(ans, 6))