cap = [chr(x) for x in range(65, 91)]
low = [x.lower() for x in cap]
while True:
    text = input()
    if text == 'end':
        break
    ciphered = ''
    for c in text:
        if c in cap:
            ciphered += cap[(cap.index(c) + 13) % 26]
        elif c in low:
            ciphered += low[(low.index(c) + 13) % 26]
        else:
            ciphered += c
    print(ciphered)