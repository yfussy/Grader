rows = [chr(i) for i in [*range(97,123),*range(65,91)]]
cols = [*range(1,53)]
board = {}
for rnum, r in enumerate(rows):
    for cnum, c in enumerate(cols):
        grid = (r,c)
        if rnum % 2 == 0:
            board[grid] = 'White' if cnum % 2 == 0 else 'Black'
        else:
            board[grid] = 'Black' if cnum % 2 == 0 else 'White' 

check = input().strip()
if len(check) <= 3:
    check = check.replace(' ','')
    row, col = check[0], check[1:]
else:
    row, col = [e.split('=')[-1].strip() for e in sorted([e.strip() for e in check.split(',')],reverse=True)]

try:
    col = int(col)
except:
    pass

errors = []
if row not in rows and col not in cols:
    print('Invalid row and column')
elif row not in rows:
    print('Invalid row')
elif col not in cols:
    print('Invalid column')
else:
    print(board[(row,col)])