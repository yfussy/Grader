word = [c for c in input()]
vowels = ['a', 'e', 'i', 'o', 'u']
match word:
    case [*c, 'x'] | [*c, 's'] | [*c, 'c', 'h']:
        word += 'es'
    case [*c, 'y'] if c[-1] not in vowels:
        word[-1] = 'ies'
    case _:
        word += 's'
print(''.join(word))