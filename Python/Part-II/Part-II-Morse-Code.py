import time

f = input()
with open(f, 'r') as fin:
    data = fin.read().splitlines()
    op, pattern, texts = data[0], data[1], data[2:]

morseMap = {}
l = 0
while l < len(pattern) - 1:
    j = l + 1
    k = pattern.find(']', j)
    l = pattern.find('[', k) 
    morseMap[pattern[j:k]] = pattern[k+1:l]

if op == 'M2T':
    morseMap = dict([(val, key) for key, val in morseMap.items()])
    texts = [text.split() for text in texts]

if op == 'M2T' or op == 'T2M':
    for text in texts:
        morse = []
        for char in text:
            if char in morseMap:
                morse.append(morseMap[char])
            else:
                morse = ['Invalid : '] + [" ".join(text) if op == 'M2T' else text]
                break
        print(''.join(morse) if op == 'M2T' else ' '.join(morse))
else:
    print('Invalid code')