def noLower(p):
    if p.islower():
        return False
    return True

def noUpper(p):
    if p.isupper():
        return False
    return True

def noNum(p):
    if any(c.isnumeric() for c in p):
        return False
    return

def noSym(p):
    if not p.isalnum():
        return False
    return True

def charRep(p):
    pass

def numSeq(p):
    p = p.lower()
    numSeq = ''.join([str(x) for x in range(10)] + ['0'])
    numSeqRe = ''.join(numSeq[::-1])
    for i in range(len(p) - 3):
        text = p[i:i+4] 
        if text in numSeq or text in numSeqRe:
            return True
    return False

def charSeq(p):
    pass

def keyPat(p):
    pass

pw = input().split()
errors = []
