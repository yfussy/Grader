nameDict = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah', 'Dick', 'Bill', 'Jim', 'Jack', 'Peggy', 'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']
n = int(input())
for i in range(n):
    name = input()
    if name in nameDict:
        print(nameDict[(nameDict.index(name)+10)%20])
    else:
        print('Not found')