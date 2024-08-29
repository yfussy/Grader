text = sorted(input().replace(' ', '').lower())
anagram = sorted(input().replace(' ', '').lower())
if text == anagram:
    print('YES')
else:
    print('NO')