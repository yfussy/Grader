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
    numSeq = ''.join([str(x) for x in range(10)] + ['0'])
    numSeqRe = numSeq[::-1]
    for i in range(len(p) - 3):
        text = p[i:i+4] 
        for seq in numSeq + numSeqRe:
            if text in seq:
                return True
    return False

def charSeq(p):
    p = p.lower()
    charSeq = ''.join([chr(x) for x in range(97,123)] + ['a'])
    charSeqRe = charSeq[::-1]
    for i in range(len(p) - 3):
        text = p[i:i+4]
        for seq in charSeq + charSeqRe:
            if text in seq:
                return True
    return False
    
def keyPat(p):
    p = p.lower()
    keySeq = ['!@#$%^&*()_+', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    keySeqRe = []
    for pat in keySeq:
        keySeqRe.append(pat[::-1])
    for i in range(len(p) - 3):
        text = p[i:i+4] 
        for pat in keySeq + keySeqRe:
            if text in pat:
                return True
    return False

pw = input().split()
errors = []
