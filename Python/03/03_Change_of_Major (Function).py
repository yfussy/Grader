def choose(stu1, stu2):

    passingGrade1 = stu1[2] == 'A' and stu1[3] <= 'C' and stu1[4] <= 'C'
    passingGrade2 = stu2[2] == 'A' and stu2[3] <= 'C' and stu2[4] <= 'C'

    if not passingGrade1 and not passingGrade2:
        return []
    elif not passingGrade1:
        return [stu2[0]]
    elif not passingGrade2:
        return [stu1[0]]
    else:
        if stu1[1:] == stu2[1:]:
            return [stu1[0], stu2[0]]
        elif [-stu1[1]] + stu1[3:] < [-stu2[1]] + stu2[3:]:
            return [stu1[0]]
        else:
            return [stu2[0]]
        
exec(input())