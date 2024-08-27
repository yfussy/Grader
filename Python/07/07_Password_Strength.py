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
    pass

def charSeq(p):
    pass

def keyPat(p):
    pass

pw = input().split()
errors = []