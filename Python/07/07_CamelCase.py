text = input().lower()
camel = ""
for char in text:
    if not char.isalnum():
        camel += " "
    else:
        camel += char
camelCase = []
for i, word in enumerate(camel.split()):
    if i == 0:
        camelCase.append(word)
        continue
    camelCase.append(word.capitalize())
print(''.join(camelCase))