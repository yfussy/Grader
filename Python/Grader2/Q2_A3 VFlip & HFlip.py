n = int(input())
img = []
for _ in range(n):
    img.append(input())
match input():
    case 'hflip':
        print(*[layer[::-1] for layer in img], sep='\n')
    case 'vflip':
        print(*img[::-1], sep='\n')