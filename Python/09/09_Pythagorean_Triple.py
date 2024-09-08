def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

def is_coprime(a, b, c):
    coprime = [a, b, c]
    for i in range(len(coprime)-1, -1, -1):
        divisor = gcd(coprime[i], coprime[i-1])
        if gcd(divisor, coprime[i-2]) != 1:
            return False
    return True

def primitive_Pythagorean_triples(max_len):
    triple = []
    for c in range(1, max_len + 1):
        for b in range(c, 0, -1):
            a = (c**2 - b**2)**0.5
            if a == int(a) and a > 0 and [c, b, a] not in triple:
                a = int(a)
                if is_coprime(a,b,c):
                    triple.append([c, a, b])
    return [[a, b, c] for c, a, b in sorted(triple)]

exec(input().strip())