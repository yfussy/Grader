h = int(input())

for i in range(1, h+1):
    layer = '.'*abs(i-h) + '*'
    if i == 1:
        print(layer)
    elif i == h:
        layer += '*'*(2*i-3) + '*'
        print(layer)
    else:
        layer += '.'*(2*i-3) + '*'
        print(layer)