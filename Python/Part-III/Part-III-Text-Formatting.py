data = input()
k = int(input())
ruler = ''
i = 0
for i in range(k//10):
    ruler += '-' * 9 + str(i+1)
ruler += '-' * (k-(10*(i+1)))
print(ruler)

with open(data, 'r') as fin:
    data = [line.replace('\n', '') for line in fin.readlines()]
    data = '.'.join(data)
words = [w for w in data.split('.') if w != '']

result = []
line = ''
start = 0
for word in words:
    wordIndex = data.find(word,start) + len(word)
    line += data[start:wordIndex]
    length = wordIndex - start
    if len(line) > k:
        line = line[:-length]
        result.append(line)
        line = word.strip('.')
    start = wordIndex
result.append(line)

print(*result, sep='\n')