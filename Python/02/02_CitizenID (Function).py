def check_digit(n):
    lastDigit = 0
    for i in range(len(n)):
        lastDigit += abs(i-13) * int(n[i])
    lastDigit = (11 - (lastDigit % 11)) % 10

    return lastDigit

exec(input())