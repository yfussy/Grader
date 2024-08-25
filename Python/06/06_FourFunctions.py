def make_int_list(x):
    return list(map(int ,x.split()))

def is_odd(e):
    if e % 2 != 0:
        return True
    return False

def odd_list(alist):
    return list(filter(is_odd, alist))

def sum_square(alist):
    return sum(map(lambda x: x**2, alist))

exec(input().strip())