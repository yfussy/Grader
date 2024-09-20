courses = input()
teachers = input()
database = input()
with open(courses,'r') as cin, open(teachers,'r') as tin, open(database, 'r') as din:
    c = [x.replace('\n', '').split(',') for x in cin.readlines()]
    t = [x.replace('\n', '').split(',') for x in tin.readlines()]
    d = [x.replace('\n', '').split(',') for x in din.readlines()]
coursesId = {info[0]:info[1] for info in c}
teachersId = {info[0]:info[1] for info in t}
for course, teacher in d:
    if course not in coursesId or teacher not in teachersId:
        print('record error')
        continue
    print(f'{coursesId[course]},{teachersId[teacher]}')