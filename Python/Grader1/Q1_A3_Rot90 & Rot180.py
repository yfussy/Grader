n = int(input())
img = []
for _ in range(n):
    layer = [x for x in input()]
    img.append(layer)
op = input()[3:]
for _ in range(int(op)//90):
    img = img[::-1]
    img = list(zip(*img))
for layer in img:
    print(''.join(layer))