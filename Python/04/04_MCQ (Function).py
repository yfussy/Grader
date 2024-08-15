def grade_mcq(sol, ans):
    if len(sol) != len(ans):
        return -1
    
    grade = 0
    for i, key in enumerate(sol):
        if key == ans[i]:
            grade += 1
    return grade

exec(input())