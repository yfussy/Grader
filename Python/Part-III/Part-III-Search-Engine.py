n = int(input())
file = {}
for _ in range(n):
    title = input()
    content = input().split()
    data = {}
    for word in content:
        if word not in data:
            data[word] = 1
        else:
            data[word] += 1
    file[title] = data

while True:
    search = input()
    scores = []
    if search == '-1':
        break
    
    for title, content in file.items():
        if search in content.keys():
            freq = content[search]/sum(content.values())
        else:
            freq = 0
        scores.append((title, freq/len(content.keys())))

    top = sorted(scores,key=lambda x: x[1], reverse=True)[0]
    if top[1] == 0:
        print('NOT FOUND')
    else:
        print(top[0])