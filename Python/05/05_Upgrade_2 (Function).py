possibleGrades = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']

def index_of(grades, ID):
    for i, grade in enumerate(grades):
        if ID in grade:
            return i
    return -1

def upgrade(grades, IDs):
    for id in IDs:
        if index_of(grades, id) == -1:
            continue
        grade = grades[index_of(grades, id)]
        grade[1] = possibleGrades[index_of(possibleGrades, grade[1]) + 1 if grade[1] != 'A' else -1]
    return grades.sort()

exec(input())
exec(input())
exec(input())