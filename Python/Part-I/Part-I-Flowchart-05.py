c = input().strip()

match c:
    case 'S':
        m = int(input())
        q = 1
        r = 0
        t = 1
        k = 1
        n = 3
        x = 3
        i = 0
        p = ""
        while i < m:
            if 4 * q + r - t < n * t:
                p += str(n)
                i += 1
                a = 10 * (r - n * t)
                n = ((10 * (3 * q + r)) // t) - (10 * n)
                q *= 10
                r = a
            else:
                a = (2 * q + r) * x
                b = (7 * q * k + 2 + x * r) // (x * t)
                q *= k
                t *= x
                x += 2
                k += 1
                n = b
                r = a
        p = p[0] + '.' + p[1:]
        print('pi =', p)
    case 'R':
        n = int(input())
        sigma = 0
        for k in range(n+1):
            nom = (-3)**(-k)
            denom = 2 * k + 1
            sigma += nom/denom
        p = round((12**0.5) * sigma, 12)
        print('pi =', p)
    case 'P':
        p = round((7 + ((6 + (5**0.5))**0.5))**0.5, 6)
        print('pi =', p)
    case _:
        print('Invalid')