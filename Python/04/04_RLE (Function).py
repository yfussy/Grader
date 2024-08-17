def RLE(t):
    if not t:
        return []
    rle = [[t[0], 0]]
    for char in t:
        if rle[-1][0] != char:
            rle.append([char, 0])
        rle[-1][1] += 1
    return rle

exec(input())