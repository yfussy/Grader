CitizinId = input()

lastDigit = 0
for i in range(len(CitizinId)):
    lastDigit += abs(i-13) * int(CitizinId[i])
lastDigit = (11 - (lastDigit % 11)) % 10

print(CitizinId[0], CitizinId[1:5], CitizinId[5:10], CitizinId[10:12], lastDigit)