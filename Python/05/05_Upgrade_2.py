possibleGrades = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
grades = []
while True:
    grade = input()
    if grade == 'q':
        break
    grade = grade.split()
    grades.append([grade[0], grade[1]])
grades.sort()
change = input().split()
for grade in grades:
    for student in change:
        if student in grade:
            grade[1] = possibleGrades[possibleGrades.index(grade[1]) + 1 if grade[1] != 'A' else -1]
            break
    print(grade[0], grade[1])