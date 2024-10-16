def hashTable(text):
    text = ''.join([x for x in text if x.isalpha()]).lower()
    table = {}
    for char in sorted(text):
        table[char] = 1 if char not in table else table[char] + 1
    return table

def showRemove(table):
    if sum(table.values()) == 0:
        print(' - None')
    for char, n in table.items():
        if n != 0:
            remove = f' - remove {str(n)} {char}'
            if n > 1:
                remove += "'s"
            print(remove)

a = input()
b = input()
aTable, bTable = hashTable(a), hashTable(b)
for char in aTable.keys():
    if char in bTable:
        n = min(aTable[char], bTable[char])
        aTable[char] -= 1 * n
        bTable[char] -= 1 * n    
        
print(a)
showRemove(aTable)
print(b)
showRemove(bTable)
