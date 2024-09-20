catas = {}
while True:
    ip = input()
    if ip == 'q':
        for cata, names in catas.items():
            print(f"{cata}: {', '.join(names)}")
        break
    name, cata = ip.split(', ')
    if cata in catas:
        catas[cata].append(name)
    else:
        catas[cata] = [name]