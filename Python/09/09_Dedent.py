rows = int(input())
for _ in range(rows):
    code = input()
    if code.find('..') == 0:
        i = 0
        while True:
            i += 1
            if code[i] != '.':
                break
        code = code[:i//2] + code[i:]
    print(code)