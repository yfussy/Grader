def knows(R, x, y):
    if y in R[x]:
        return True
    return False

def is_celeb(R, x):
    for ppl in R:
        if ppl == x:
            if len(R[ppl]) > 1 or (len(R[ppl]) == 1 and x not in R[ppl]):
                return False
        else:
            if not knows(R, ppl, x):
                return False
    return True
 
def find_celeb(R):
    for ppl in R:
        if is_celeb(R, ppl):
            return ppl
    return None

def read_relations():
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1:
            break
        name, know = d
        if know not in R:
            R[know] = set()
        if name not in R:
            R[name] = {know}
        else:
            R[name].add(know)
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None:
        print('Not Found')
    else:
        print(c)

exec(input().strip())