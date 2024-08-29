def noLower(p):
    for c in p:
        if c.islower():
            return False
    return True

def noUpper(p):
    for c in p:
        if c.isupper():
            return False
    return True

def noNum(p):
    if any(c.isnumeric() for c in p):
        return False
    return True

def noSym(p):
    if not p.isalnum():
        return False
    return True

def charRep(p):
    p = p.lower()
    prev = ""
    i = 0
    for char in p:
        if char == prev:
            i += 1
        else:
            i = 1
        if i == 4:
            return True
        prev = char
    return False

def numSeq(p):
    p = p.lower()
    i = 0
    for i in range(len(p) - 4):
        if p[i].isalpha() and p[i].isalpha():
            continue
        print(ord(p[i]), ord(p[i+1]))
        if abs(ord(p[i])-ord(p[i+1])) == 1:
            i += 1
        else:
            i = 1
        if i == 4:
            return True
    return False

def charSeq(p):
    p = p.lower()
    i = 0
    for i in range(len(p) - 4):
        if p[i].isnumeric() or p[i+1].isnumeric():
            continue
        if abs(ord(p[i])-ord(p[i+1])) == 1:
            i += 1
        else:
            i = 1
        if i == 4:
            return True
    return False

def keyPat(p):
    p = p.lower()
    keyPattern = ['!@#$%^&*()_+', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    for pattern in keyPattern:
        for i in range(len(p) - 4):
            if p[i] + p[i+1] + p[i+2] + p[i+3] in pattern:
                return True
    return False

pw = input().strip()
err = []
if len(pw) < 8:
    err.append('Less than 8 characters')
if noLower(pw):
    err.append('No lowercase letters')
if noUpper(pw):
    err.append('No uppercase letters')
if noNum(pw):
    err.append('No numbers')
if noSym(pw):
    err.append('No symbols')
if charRep(pw):
    err.append('Character repitition')
if numSeq(pw):
    err.append('Number sequence')
if charSeq(pw):
    err.append('Letter sequence')
if keyPat(pw):
    err.append('Keyboard pattern')
if len(err) == 0:
    err.append('OK')
for er in err:
    print(er)