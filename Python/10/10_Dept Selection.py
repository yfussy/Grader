n = int(input())
dept = {}
for _ in range(n):
    branch, amount = input().split()
    dept[branch] = int(amount)

n = int(input())
students = []
for _ in range(n):
    sid, grade, *rank = input().split()
    students.append([float(grade), sid, rank])

for s in sorted(students, reverse=True):
    grade, sid, rank = s
    for ranking in rank:
        if dept[ranking] != 0:
            students[students.index(s)] = [sid, ranking]
            dept[ranking] -= 1
            break

for sid, branch in sorted(students):
    print(sid, branch)