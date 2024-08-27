def readNext(file):
    while True:
        text = file.readline()
        if len(text) == 0:
            return ["",""]
        return text.strip().split()

f1, f2 = input().split()
fin1 = open(f1, 'r')
fin2 = open(f2, 'r')

student1 = readNext(fin1)
student2 = readNext(fin2)

while student1 != ["",""] and student2 != ["",""]:
    if student1[0][-2:] < student2[0][-2:]:
        print(' '.join(student1))
        student1 = readNext(fin1)
    elif student1[0][-2:] > student2[0][-2:]:
        print(' '.join(student2))
        student2 = readNext(fin2)
    else:
        if student1 < student2:
            print(' '.join(student1))
            student1 = readNext(fin1)
        else:
            print(' '.join(student2))
            student2 = readNext(fin2)
        
while student1 != ["",""]:
    print(' '.join(student1))
    student1 = readNext(fin1)
while student2 != ["",""]:
    print(' '.join(student2))
    student2 = readNext(fin2)