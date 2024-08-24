text = input()
missing = []
for i in range(10):
    if str(i) not in text:
        missing.append(str(i))
if missing:
    print(','.join(missing))
else:
    print('None')