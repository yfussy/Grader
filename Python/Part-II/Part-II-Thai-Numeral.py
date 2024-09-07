def to_Thai(N):
    lek = {
        '0': 'soon',
        '1': ['neung', 'et'],
        '2': ['song', 'yi'],
        '3': 'sam',
        '4': 'si',
        '5': 'ha',
        '6': 'hok',
        '7': 'chet',
        '8': 'paet',
        '9': 'kao',
    }
    lak = {
        2: 'sip',
        3: 'roi',
        4: 'pun'
    }
    arn = ""
    N = str(N)
    leklak = len(N)
    for num in N:
        if num == '2':
            arn += lek[num][1 if leklak == 2 else 0] + ' '
        elif num == '1':
            if leklak != 2:   
                arn += lek[num][1 if (leklak == 1 and len(N) != 1) else 0] + ' '
        elif num == '0':
            if len(N) == 1:
                arn += lek[num]
            leklak -= 1
            continue
        else:
            arn += lek[num] + ' '

        if leklak != 1:
            arn += lak[leklak] + ' '
            leklak -= 1
    return arn

exec(input())