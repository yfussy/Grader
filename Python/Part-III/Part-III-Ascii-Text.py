file = input()
op = input()

def rotate(l, dir):
    # 1:cw -1:ccw
    return [''.join(t) for t in list(zip(*l[::-dir]))[::dir]]

def strip(l, dir, full=False):
    # 1:left -1:right
    l = rotate(l, dir)
    i = 0
    for _ in range(len(l[:])):
        if all(t == '.' for t in l[i]):
            l.pop(i)
            continue
        if not full:
            break
        i += 1
    return rotate(l, -dir)

with open(file, 'r') as fin:
    text = [line.replace('\n', '') for line in fin.readlines()]

match op:
    case 'LSTRIP':
        print(*(strip(text, 1)), sep='\n')
    case 'RSTRIP':
        print(*(strip(text, -1)), sep='\n')
    case 'STRIP':
        print(*(strip(strip(text, -1), 1)), sep='\n')
    case 'STRIP_ALL':
        print(*(strip(text, 1, full=True)), sep='\n')
    case _:
        print('Invalid command')