incripted = input()

decriptKey = {1: 'A',
              2: 'B',
              3: 'C',
              4: 'D',
              5: 'E',
              6: 'F',
              7: 'G',
              8: 'H',
              9: 'I',
              10: 'J',}

decripting1 = ""
for i in range(3, 32, 7):
    decripting1 += incripted[i]

decripting2 = ""
for i in range(7, 32, 5):
    decripting2 += incripted[i]

decripting3 = int(decripting1) + int(decripting2) + 10000

decripting4 = ""
for i in range(3):
    decripting4 += str(decripting3)[i-4]

decripting5 = 0
for num in decripting4:
    decripting5 += int(num)

decripting6 = int(str(decripting5)[-1]) + 1
decripting6 = decriptKey[decripting6]

decripted = decripting4 + decripting6

print(decripted)