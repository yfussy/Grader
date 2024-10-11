n = int(input())
k = int(input())
errors = []
if n < 1 and isinstance(n, int):
    errors.append('n')
if k < 1:
    errors.append('k')
if errors:
    if len(errors) == 1:
        print(f'Invalid {errors[0]}')
    else:
        print('Invalid n and k')
else:
    pos = []
    for i in range(1, k+1):
        layer = str(i) + '-'*(n - len(str(i)) + 1)
        if i == k:
            layer = layer[:-1]
        pos.append(layer)
    print(''.join(pos))

    grays = ['0', '1']
    while len(grays[0]) < n:
        reverse = []
        for i, num in enumerate(grays):
            grays[i] = '0' + num
            reverse.insert(0, '1' + num)
        grays += reverse
    i = 0
    for j in range(k,len(grays), k):
        print(','.join(grays[i:j]))
        i = j
    if i < len(grays):
        print(','.join(grays[i:]))