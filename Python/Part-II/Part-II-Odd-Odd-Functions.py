def is_odd(n):
    return True if n % 2 != 0 else False

def has_odds(x):
    for num in x:
        if is_odd(num):
            return True
    return False

def all_odds(x):
    for num in x:
        if not is_odd(num):
            return False
    return True

def no_odds(x):
    return not has_odds(x)

def get_odds(x):
    odds = []
    for num in x:
        if is_odd(num):
            odds.append(num)
    return odds

def zip_odds(a, b):
    zipOdd = []
    oddA = get_odds(a)
    oddB = get_odds(b)
    minLen = min(len(oddA), len(oddB))
    for i in range(minLen):
        zipOdd.append(oddA[i])
        zipOdd.append(oddB[i])
    return zipOdd + (oddA[minLen:] if minLen == len(oddB) else oddB[minLen:])

exec(input().strip()) 