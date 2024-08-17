parantheses = {
    '(': '[',
    ')': ']',
    '[': '(',
    ']': ')',
}

text = input()
out = ""
for i, char in enumerate(text):
    if char in parantheses:
        out += parantheses[char]
        continue
    out += char
    
print(out)