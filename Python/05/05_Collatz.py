n = int(input())
log = [n]
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3*n + 1
    log.append(n)
if len(log) > 15:
    log = log[-15:]
ans = f'{log[0]}'
for num in log[1:]:
    ans += f'->{num}'
print(ans)