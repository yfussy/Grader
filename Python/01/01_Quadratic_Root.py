a  = float(input())
b  = float(input())
c  = float(input())

sqrt = (b**2 - (4*a*c))**(1/2)

x1 = (-b - sqrt)/(2*a)
x2 = (-b + sqrt)/(2*a)

print(round(x1, 3), round(x2, 3))