x, y = map(int, input().split())
minZig = x
maxZig = y
minZag = y
maxZag = x
i = 1

while True:
    nums = input().split()
    if len(nums) == 1:
        break

    x, y = map(int, nums)

    if i % 2 == 1:
        x, y = y, x

    minZig = min(minZig, x)
    maxZig = max(maxZig, y)
    minZag = min(minZag, y)
    maxZag = max(maxZag, x)

    i += 1

if nums[0] == "Zig-Zag":
    print(minZig, maxZig)
else:
    print(minZag, maxZag)