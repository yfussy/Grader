key = input()
ans = input()
score = 0

if len(key) == len(ans):
    for i in range(len(key)):
        if ans[i] == key[i]:
            score += 1
    print(score)
else:
    print("Incomplete answer")