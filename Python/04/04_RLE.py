t = input()

rle = [t[0], 0]
for char in t:
    if rle[-2] != char:
        rle.append(char)
        rle.append(0)
    rle[-1] += 1

print(' '.join(map(str, rle)))