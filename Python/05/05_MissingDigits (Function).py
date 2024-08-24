def missing_digits(t):
    missing = []
    for i in range(10):
        if str(i) not in t:
            missing.append(i)
    return missing
exec(input())