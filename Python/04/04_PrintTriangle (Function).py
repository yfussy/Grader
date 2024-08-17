def print_triangle(h):
    triangle = []
    for i in range(1, h+1):
        layer = '.'*abs(i-h) + '*'
        if i == 1:
            pass
        elif i == h:
            layer += '*'*(2*i-3) + '*'
        else:
            layer += '.'*(2*i-3) + '*'
        triangle.append(layer)
    print('\n'.join(triangle))

exec(input())