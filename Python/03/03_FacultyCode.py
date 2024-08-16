avaliableFalc = ['01',
                 '02',
                 '51',
                 '53',
                 '55',
                 '58',]

for i in range(20, 41):
    avaliableFalc.append(str(i))
    
code = input()

if code in avaliableFalc:
    print("OK")
else:
    print("Error")