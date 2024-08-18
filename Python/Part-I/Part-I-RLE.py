operations = ['str2RLE', 'RLE2str']
op = input()
if op in operations:
    t = input()
    if op == operations[0]:
        rle = [t[0], 0]
        for char in t:
            if rle[-2] != char:
                rle.append(char)
                rle.append(0)
            rle[-1] += 1

        print(' '.join(map(str, rle)))
    else:
        t = t.split()
        toStr = []
        for i in range(0, len(t), 2):
            toStr.append(t[i]*int(t[i+1]))
        print(''.join(toStr))
else:
    print('Error')