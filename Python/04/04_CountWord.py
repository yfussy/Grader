check = input()
text = input() + ' '
word = ""
repeat = 0
wordSeparator = [' ','"', '(', ')', ',', '.', "'"]
for char in text:
    if char in wordSeparator:
        if word == check:
            repeat += 1
        word = ""
        continue
    word += char

print(repeat)  