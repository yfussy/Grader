otas = []
idols = []
scores = []
while True:
    data = input().split()
    if len(data) == 1:
        op = data[0]
        break
    ota, idol, score = data
    otas.append(ota)
    idols.append(idol)
    scores.append(int(score))

match op:
    case '1':
        vote = {}
        for i, idol in enumerate(idols):
            if idol not in vote:
                vote[idol] = scores[i]
            else:
                vote[idol] += scores[i]
        result = [name for name,_ in sorted(vote.items(), key=lambda x: x[1], reverse=True)]
    case '2':
        vote = {}
        for i, idol in enumerate(idols):
            if idol not in vote:
                vote[idol] = {otas[i]}
            else:
                vote[idol].add(otas[i])
        result = [name for name,_ in sorted(vote.items(), key=lambda x: len(x[1]), reverse=True)]
    case '3':
        kamiOshi = {}
        for i, ota in enumerate(otas):
            oshi = [scores[i], idols[i]]
            if ota not in kamiOshi:
                kamiOshi[ota] = [oshi]
            else:
                for pair in kamiOshi[ota]:
                    if pair[1] == oshi[1]:
                        pair[0] += oshi[0]
                else:
                    kamiOshi[ota].append(oshi)
        kamiOshi = {ota: sorted(oshi, key=lambda x: (-x[0], x[1]))[0][1] for ota,oshi in kamiOshi.items()}
        oshiCount = {idol: 0 for idol in idols}
        for idol in kamiOshi.values():
            oshiCount[idol] += 1
        result = [oshi for oshi,_ in sorted(oshiCount.items(), key=lambda x: x[1], reverse=True)]
print(', '.join(result[:3]))