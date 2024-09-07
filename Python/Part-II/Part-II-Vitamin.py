n = int(input())
fruit = []
for _ in range(n):
    data = input().split()
    fruit.append(data)

op = input().split()
match op[0]:
    case 'show':
        for data in fruit:
            print(' '.join(data))
    case 'get':
        if op[1] not in [data[0] for data in fruit]:
            print(f'{op[1]} not found')
        else:
            for data in fruit:
                if data[0] == op[1]:
                    print(' '.join(data))
        
    case 'avg':
        dataInfo = [float(data[int(op[1])]) for data in fruit]
        print(round(sum(dataInfo)/len(dataInfo), 4))
    case 'max':
        dataInfo = sorted([data[int(op[1])] for data in fruit])
        dataInfoPair = sorted([[data[int(op[1])], data[0]] for data in fruit])
        maxData = max(dataInfoPair)
        print(dataInfoPair[dataInfo.index(maxData[0])][1], maxData[0])
    case 'sort':
        dataInfoPair = sorted([[data[int(op[1])], data[0]] for data in fruit])
        print(' '.join([name for _, name in dataInfoPair]))