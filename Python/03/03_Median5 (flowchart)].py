nums = []
for i in range(5):
    nums.append(int(input()))
a, b, c, d, e = nums
if a > b:
    a, b = b, a
if c > d:
    c, d = d, c
if a > c:
    b, d = d, b
    c = a
a = e
if a > b:
    a, b = b, a
if c > a:
    b, d = d, b
    a = c
if a > d:
    print(d)
else:
    print(a)