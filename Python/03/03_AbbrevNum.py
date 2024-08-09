num = int(input())

abbrev = {
    3: 'K',
    6: 'M',
    9: 'B'
}

abbrevNum = 0
for i in range(9,2,-3):
    if num / 10**i > 1:
        if num / 10**i > 10:
            abbrevNum = str(round(num / 10**i)) + abbrev[i]
            break
        else:
            abbrevNum = str(round(num / 10**i, 1)) + abbrev[i]
            break

if not abbrevNum:
    abbrevNum = num

print(abbrevNum)