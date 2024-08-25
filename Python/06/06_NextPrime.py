def is_prime(n):
    if n <= 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(N):
    while True:
        N += 1
        if is_prime(N):
            return N

def next_twin_prime(N):
    while True:
        if is_prime(next_prime(N) + 2):
            return next_prime(N), next_prime(N) + 2
        N = next_prime(N)

exec(input())