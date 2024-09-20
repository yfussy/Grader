n = int(input())
win = set()
lose = set()
for _ in range(n):
    w, l = input().split()
    win.add(w)
    lose.add(l)
win.difference_update(lose)
print(sorted(win))