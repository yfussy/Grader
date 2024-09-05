def reverse(d):
    d = dict([(val, key) for key, val in d.items()])
    return d

def keys(d, v):
    matchKey = [key for key, val in d.items() if val == v]
    return matchKey

exec(input().strip())