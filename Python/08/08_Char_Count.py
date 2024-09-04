text = input().lower()
hashT = {}
for char in text:
    if not char.isalpha():
        continue
    if char not in hashT:
        hashT[char] = 0
    hashT[char] += 1
count = sorted([[-val, key] for key, val in hashT.items()])
for char in count:
    print(f'{char[1]} -> {abs(char[0])}')