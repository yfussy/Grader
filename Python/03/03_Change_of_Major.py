student1 = input().split()
student2 = input().split()

student1[1] = float(student1[1])
student2[1] = float(student2[1])

passingGrade1 = student1[2] == 'A' and student1[3] <= 'C' and student1[4] <= 'C'
passingGrade2 = student2[2] == 'A' and student2[3] <= 'C' and student2[4] <= 'C'

if not passingGrade1 and not passingGrade2:
    print('None')
elif not passingGrade1:
    print(student2[0])
elif not passingGrade2:
    print(student1[0])
else:
    if student1[1:] == student2[1:]:
        print('Both')
    elif [-student1[1]] + student1[3:] < [-student2[1]] + student2[3:]:
        print(student1[0])
    else:
        print(student2[0])