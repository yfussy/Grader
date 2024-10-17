target = input().lower()
n = int(input())
layers = []
for _ in range(n):
    layers.append(input())
S = '|'.join(layers)

pointer = 0
finds = []
while True:
    start = S.replace('|', ' ').lower().find(target, pointer)
    if start == -1:
        break
    pointer = start + len(target)
    S = S[:start] + "<found>" + S[start:pointer] + "</found>" + S[pointer:]
    pointer += 15
print(*S.split('|'), sep='\n')