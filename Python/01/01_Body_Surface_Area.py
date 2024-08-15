import math

w = float(input())
h = float(input())

mosteller = (math.sqrt(w*h)) / 60 
haycock = 0.024265 * (w ** 0.5378) * (h ** 0.3964)
boyd = 0.0333 * w**(0.6157-(0.0188 * math.log10(w))) * h**0.3
print(mosteller)
print(haycock)
print(boyd)