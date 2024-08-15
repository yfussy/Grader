x = ""
y = ""
l = 0

while True:
    nums = input().split()
    if len(nums) == 1:
        operation = 1 if "Zig-Zag" in nums else -1
        break       
    x += nums[0] + ' '
    y += nums[1] + ' '
    l += 1

min = None
max = None 
for i in range(l):
    minLine = ''
    maxLine = ''

    if operation == 1:
        while x[0] != ' ':
            minLine += x[0]
            x = x[1:]
        while y[0] != ' ':
            maxLine += y[0]
            y = y[1:]
    else:
        while x[0] != ' ':
            maxLine += x[0]
            x = x[1:]
        while y[0] != ' ':
            minLine += y[0]
            y = y[1:]
    
    x = x[1:]
    y = y[1:]
    
    minLine = int(minLine)
    maxLine = int(maxLine)
    operation *= -1

    if not min and not max:
        min = int(minLine)
        max = int(maxLine)
        continue
    else:
        min = min(min, minLine)
        max = max(max, maxLine)

print(min, max)